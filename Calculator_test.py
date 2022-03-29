import Calculator

import pytest

@pytest.mark.parametrize("x,y,z",[(3,2,5),(5,1,6),(8,2,10),(5,2,9)])
def test_add2no(x,y,z):

    res = Calculator.add2no(x,y)
    assert res == z

@pytest.mark.parametrize("x,y,z",[(20,30,40),(5,1,6),(8,2,10)])
def test_sub2no(x,y,z):

    res = Calculator.sub2no(x, y)
    assert res == z

@pytest.mark.parametrize("x,y,z",[(3,2,5),(10,20,40),(8,2,10)])
def test_mul2no(x,y,z):

    res = Calculator.mul2no(x, y)
    assert res == z

@pytest.mark.parametrize("x,y,z",[(3,2,5),(5,1,6),(20,30,40)])
def test_div2no(x,y,z):

    res = Calculator.div2no(x, y)
    assert res == z



