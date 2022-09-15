import pytest


class TestDemo:
    data_list = ["one", "two"]

    @pytest.mark.parametrize("name", data_list)
    def test_a(self, name):
        print(name)


if __name__ == '__main__':
    pytest.main(["-s", "pytest_one.py"])