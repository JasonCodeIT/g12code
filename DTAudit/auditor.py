from pipe import JSONPipe
import requests
import re
import os
import json
from urlparse import urlparse
from urlparse import parse_qsl


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
                self.login(endpoint)

            for payload in incomings[1]:
                exploitable, exploit = self.exploit(endpoint, payload)

                if exploitable:
                    counter += 1
                    exploits.append({
                        'name': 'exploit-' + str(counter),
                        'exploit': exploit
                    })
                    print "found exploit, skip other payload"
                    break

        return exploits

    def login(self, endpoint):

        seed = endpoint['seed']

        if seed not in self.session:
            self.session[seed] = {
                "login": False,
                "token": None
            }
        else:
            return

        auth = self.seeds[seed]['auth']

        if auth:
            self.http.get(auth['url'], verify=False)
            r = self.http.post(auth['target'], data=auth['params'], verify=False)
            if 'token' in auth:
                self.session[seed]['token'] = parse_token(r.request.url, auth['token'])
            self.session[seed]['login'] = True

    def exploit(self, endpoint, payload):
        exploit = []

        method = endpoint['method'].upper()
        target = endpoint['target']
        params = endpoint['params']

        entrance = endpoint['url'] if 'url' in endpoint else endpoint['target']

        files = {}
        file_fields = {}

        print method, ": ", target

        for key in params:
            if endpoint['files'] and key in endpoint['files']:
                files[key] = open(self.filePath, 'rb')

        if files:
            for k in files:
                file_fields[k] = os.path.abspath(files[k].name)

        bundles = self.prepare_bundles(params, payload)

        found = False

        print bundles

        for bundle in bundles:

            for key in params:
                if endpoint['files'] and key in endpoint['files']:
                    bundle.pop(key, None)

            print "attempting:", bundle, file_fields

            if method == 'GET':
                r = self.http.get(target, params=bundle, verify=False)
            else:
                r = self.http.post(target, data=bundle, files=files, verify=False)

            exploitable, exp = self.verify(r, target)

            if exploitable:
                found = True
                break

        if found:
            if method == 'GET':
                query = ''
                for k in bundle:
                    query += "%s=%s&" % (k, bundle[k])
                exploit.append({
                    'url': target + "?" + query,
                    'formFields': None,
                    'fileFields': None
                })
            elif method == 'POST':
                exploit.append({
                    'url': entrance,
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
            links = self.find_links(response.text, referer)

            for link in links:
                if re.search('logout', link):
                    print "Skip: ", link
                    continue
                r = self.http.get(link)
                if self.see_root(r.text):
                    exploit.append({
                        'url': link,
                        'formFields': None
                    })
                    return True, exploit

        return False, exploit

    def see_root(self, text):
        return self.verificationPattern.search(re.sub('<[^>]*>', '', text))

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

    def prepare_bundles(self, params, payload):

        keys = params.keys()
        bundles = []
        bundle = {}

        if len(payload) == 1:
            for key in keys:
                bundle[key] = payload[0]
            bundles.append(bundle)

        elif len(payload) == 2:
            if len(keys) == 1:
                bundles.append({keys[0]: "".join(payload)})
            for i in range(0, len(keys)):
                bundle = {keys[i]: payload[0]}
                for j in range(i+1, len(keys)):
                    bundle[keys[j]] = payload[1]
                    for key in keys:
                        if key not in bundle:
                            bundle[key] = payload[0]
                    bundles.append(bundle)

        print payload, params, bundle, bundles

        return bundles
