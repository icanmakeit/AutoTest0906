import requests


def requests_get(url, headers=None):
    r = requests.get(url, headers=headers)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text

    res = dict()
    res["code"] = code
    res["body"] = body

    return res


def requests_post(url, json=None, headers=None):
    r = requests.post(url, json=json, headers=headers)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text

    res = dict()
    res["code"] = code
    res["body"] = body
    return res


class Request:
    def request_api(self, url, data=None, json=None, headers=None,cookies=None,method='get'):
        if method == 'get':
            r = requests.get(url, data=data,json=json,headers=headers,cookies=cookies)
        elif method == "post":
            r = requests.post(url, data=data,json=json, headers=headers,cookies=cookies)

        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        res = dict()
        res['code'] = code
        res['body'] = body

        return res

    def get(self, url, **kwargs):
        return self.request_api(url, method='get', **kwargs)

    def post(self, url, **kwargs):
        return self.request_api(url, method="post", **kwargs)














