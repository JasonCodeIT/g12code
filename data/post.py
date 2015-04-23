import requests
import json
from urlparse import urlparse
from urlparse import parse_qsl
import re


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


def post(url, data=None, cookies=None):
    r = requests.post(url, data=data, cookies=cookies, verify=False)

    return r.text.encode('utf-8')

steps = json.loads('{{{ steps }}}')

for step in steps:

    content = post(step['url'], step['formFields'], step['cookies'])

print content