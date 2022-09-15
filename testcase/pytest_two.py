import pytest


class TestDemo:
    data_list = [("xiaoming", "123"), ("xiaohong", "123")]

    @pytest.mark.parametrize(("name", "password"), data_list)
    def test_a(self, name, password):
        print(name, password)


if __name__ == '__main__':
    pytest.main(["-s", "pytest_two.py"])