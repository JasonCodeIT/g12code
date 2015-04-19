from pipe import JSONPipe
import requests
import re
import os


class auditor(JSONPipe):
    """Inject payloads to each endpoint and check if there is any vulnerability.
    """

    def __init__(self):
        self.verificationPattern = re.compile('root:(.*):0:0')
        self.linkPattern = re.compile('(href|src)="?([^\">]*)"?')
        self.filePath = 'data/image.jpg'
        self.http = requests.Session()
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
            for payload in incomings[1]:
                exploitable, exploit = self.exploit(endpoint, payload)

                if exploitable:
                    counter += 1
                    exploits.append({
                        'name': 'exploit-' + str(counter),
                        'exploit': exploit
                    })
                    break
            print "found exploit, skip other payload"

        return exploits

    def exploit(self, endpoint, payload):
        exploit = []

        method = endpoint['method'].upper()
        target = endpoint['target']
        params = endpoint['params']

        entrance = endpoint['url'] if 'url' in endpoint else endpoint['target']

        bundle = {}
        files = {}
        file_fields = {}

        print method, ": ", target

        for key in params:
            if params[key] == "":
                bundle[key] = payload
            else:
                bundle[key] = params[key]

            if endpoint['files'] and key in endpoint['files']:
                bundle.pop(key, None)
                files[key] = open(self.filePath, 'rb')

        print bundle, files

        if files:
            for k in files:
                file_fields[k] = os.path.abspath(files[k].name)

        if method == 'GET':
            query = ''
            for k in bundle:
                query += "%s=%s&" % (k, bundle[k])
            exploit.append({
                'url': target + "?" + query,
                'formFields': None
            })
            r = self.http.get(target, params=bundle, verify=False)
        elif method == 'POST':
            if entrance:
                exploit.append({
                    'url': entrance,
                    'formFields': bundle,
                    'fileFields': file_fields
                })
            r = self.http.post(target, params=bundle, files=files, verify=False)
        # Ignore COOKIE for now
        else:
            return False, []

        exploitable, exp = self.verify(r, target)

        print 'exploitable: ', exploitable

        return exploitable, exploit + exp

    def verify(self, response, referer):

        exploit = []

        if self.see_root(response.text):
            return True, exploit
        else:
            links = self.find_links(response.text, referer)

            print links

            for link in links:
                if re.search('logout', link):
                    print "Skip: ", link
                    continue
                print "GET: ", link
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
