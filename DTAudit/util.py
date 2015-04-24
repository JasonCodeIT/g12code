
import requests
import lxml.html
from urlparse import urlparse
from urlparse import parse_qsl
from scrapy import Selector


class Colors:
    def __init__(self):
        pass

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Hunter:

    def __init__(self, seed, seed_number):
        self.seed = seed
        self.seed_number = seed_number
        self.http = requests.Session()

    def hunt(self):

        # Holes can be injected
        holes = []

        auth = self.seed['auth']

        print "Hunter login with: ", auth
        params = self.seed['auth']['params'].copy()
        page = self.http.get(auth['url'], verify=False)
        html = lxml.html.document_fromstring(str(page.text.encode('utf-8')))
        inputs = html.xpath("//input[@type='hidden']")
        if 'grabs' in auth and auth['grabs']:
            for field in inputs:
                if field.name in auth['grabs']:
                    auth['params'][field.name] = field.value

        r = self.http.post(auth['target'], data=auth['params'], verify=False)

        # print r.text.encode('utf-8')

        links = self.grab_links(r)

        for link in links:
            o = urlparse(link)
            q = parse_qsl(o.query)
            bundle = {}

            for name, value in q:
                bundle[name] = value

            hole = {
                'seed': self.seed_number,
                'method': 'GET',
                'url': link,
                'target': link,
                'params': bundle,
                'files': None
            }

            holes.append(hole)

        return holes

    def grab_links(self, response):
        links = []

        html = lxml.html.document_fromstring(str(response.text.encode('utf-8')))
        tags = html.xpath("//a")

        o = urlparse(response.request.url)

        origin = o.scheme + '://' + o.hostname
        base = origin + o.path[:o.path.rfind('/')]

        for tag in tags:
            if 'href' in tag.attrib:
                path = tag.attrib['href']
            else:
                continue

            if path.find('logout') is not -1:
                continue
            if path[:4] == 'http':
                links.append(path)
                continue
            if path[:1] == '/':
                links.append(origin + path)
            else:
                links.append(base + path)

        return links
