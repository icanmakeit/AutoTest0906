import requests
from utils.RequestsUtil import requests_post, Request
from config.Conf import ConfigYaml
from utils.AssertUtil import AssertUtil


def login():
    # url = "http://121.41.14.39:2001/token/token"
    url = ConfigYaml().get_conf_url() + "/token/token"
    data = {"mobile": "13588000000", "password":"5c4fcc5add5d087de1e8534189c687f7"}
    # r = requests.post(url, data=data)
    r = Request().post(url, data=data)
    # print(r.status_code)

    # print(r.json())
    code = r["code"]
    print(r["body"]["msg"])
    print(r)
    print(code)
    # AssertUtil().assert_code(code, 100)


def order_list():
    url = "http://121.41.14.39:2001/goods/Jlist"
    r = requests.get(url)
    print(r.status_code)
    print(r.json())


def detail():
    url = "http://121.41.14.39:2001/goods/detail/1"
    r = requests.get(url)
    print(r.json())


def info():
    url = "http://121.41.14.39:2001/goods/myOrders"

    headers = {
        'Cookie': 'token=0169883341e340abbdbde82a39fd856b'
    }

    r = requests.get(url)
    print(r.json())


def miaosha():
    url = "http://121.41.14.39:2001/miaosha/miaosha"
    data = {
        "goodsId": 6,
        "token": "c1fdf6d373a44c589f686f89bf9079qq"
    }
    r = requests.post(url, data=data)
    print(r.json())


if __name__ == '__main__':
    # login()
    # # order_list()
    # # info()
    # detail()
    miaosha()