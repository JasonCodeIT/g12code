import requests


def post(url, data=None, cookies=None):
    r = requests.post(url, data=data, cookies=cookies, verify=False)

    return r.text.encode('utf-8')

steps = json.loads('{{{ steps }}}')

step = steps[0]

content = post(step['url'], step['formFields'], step['cookies'])

print content