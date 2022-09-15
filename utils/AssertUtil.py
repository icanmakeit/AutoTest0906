from utils.LogUtil import my_log
import json


class AssertUtil:
    def __init__(self):
        self.log = my_log("AssertUtil")

    def assert_code(self, code, expected_code):
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error("code error,code is %s, expected_code id %s" % (code, expected_code))
            raise

    def assert_body(self, body, expected_body):
        try:
            assert body == expected_body
        except:
            self.log.error("body error, body is %s, except_body is %s" % (str(body), str(expected_body)))
            raise

    def assert_in_body(self, body, expected_body):
        try:
            # body = json.dumps(body)
            body = body
            assert body in expected_body
        except:
            self.log.error("不包含或者body是错误的，body is %s, except_body is %s"% (body, expected_body))
            raise

