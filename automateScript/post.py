import requests


def post(url, data=None, cookies=None):
    r = requests.post(url, data=data, cookies=cookies, verify=False)

    return r.text.encode('utf-8')