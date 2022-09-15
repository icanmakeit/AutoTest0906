from config import Conf
from utils.YamlUtil import YamlReader
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
import os
import pytest


test_file = os.path.join(Conf.get_data_path(), "testlogin.yml")
print("test_file: %s" % test_file)
data_list = YamlReader(test_file).data_all()
print("data_list: %s" % data_list)


@pytest.mark.parametrize("login", data_list)
def test_yaml(login):
    print(login)
    url = ConfigYaml().get_conf_url() + login["url"]
    print(login['url'])
    data = login['data']
    request = Request()
    res = request.post(url, data=data)
    print(res)


if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])



