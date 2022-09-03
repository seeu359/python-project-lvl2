import pytest


@pytest.fixture()
def _result_stylish_simple():
    with open('tests/fixtures/result_stylish_simple') as rss:
        result_stylish_simple = rss.read()
    return result_stylish_simple


@pytest.fixture()
def _result_plain_simple():
    with open('tests/fixtures/result_plain_simple') as rps:
        result_plain_simple = rps.read()
    return result_plain_simple


@pytest.fixture()
def _result_stylish_nested1():
    with open('tests/fixtures/result_stylish_nested') as rsn1:
        result_stylish_nested1 = rsn1.read()
    return result_stylish_nested1


@pytest.fixture()
def _result_stylish_nested2():
    with open('tests/fixtures/result_stylish_nested2') as rsn2:
        result_stylish_nested2 = rsn2.read()
    return result_stylish_nested2


@pytest.fixture()
def _result_plain_nested1():
    with open('tests/fixtures/result_plain_nested') as rpn1:
        result_plain_nested1 = rpn1.read()
    return result_plain_nested1


@pytest.fixture()
def _result_plain_nested2():
    with open('tests/fixtures/result_plain_nested2') as rpn2:
        result_plain_nested2 = rpn2.read()
    return result_plain_nested2
