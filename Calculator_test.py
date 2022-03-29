import Calculator

import pytest

@pytest.mark.parametrize("x,y,z",[(3,2,5),(5,1,6),(8,2,10),(5,2,9)])
def test_add2no(x,y,z):

    res = Calculator.add2no(x,y)
    assert res == z

@pytest.mark.addsub
def test_sub2no():
    x = 20
    y = 10
    res = Calculator.sub2no(x, y)
    assert res == x - y

@pytest.mark.muldiv
def test_mul2no():
    x = 20
    y = 10
    res = Calculator.mul2no(x, y)
    assert res == x * y

@pytest.mark.muldiv
def test_div2no():
    x = 20
    y = 10
    res = Calculator.div2no(x, y)
    assert res == x / y



