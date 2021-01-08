import yaml
import pytest
import calculator


def get_datas(path):
    with open(path) as f:
        cases = yaml.safe_load(f)
        return cases


@pytest.mark.parametrize("a,b,excepted", [(1, 2, 3), (-1, -3, -4), (100, 200, 900)], ids=["int", "minus", "bigint"])
def test_add(a, b, excepted):
    print(f"add_result:{a + b}")
    assert calculator.add(a, b) == excepted


TestCases = get_datas("./data.yaml")
datas = TestCases["datas"]
ids = TestCases["myid"]


@pytest.mark.parametrize("a,b,excepted", datas, ids=ids)
def test_add_yaml(a, b, excepted):
    print(f"add_result:{a + b}")
    assert calculator.add(a, b) == excepted


def test_sub(a, b, excepted):
    assert calculator.sub(a, b) == excepted


def test_mul(a, b, excepted):
    assert calculator.mul(a, b) == excepted


def test_div(a, b, excepted):
    assert calculator.div(a, b) == excepted
