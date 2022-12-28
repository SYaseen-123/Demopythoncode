import pytest
@pytest.fixture
def numbers():
    x,y,z=10,20,30
    return[x,y,z]
def testfunction1(numbers):
    a=10
    assert numbers[0]==a
@pytest.mark.skip
def test_function2(numbers):
    a="x"
    assert number[1]==a
@pytest.mark.xfail
def test_function3(numbers):
    a=0
    assert numbers[1]==a

@pytest.mark.parametrize("a,b,c",[(1,2,3),(7,8,15)])
def test_functionAdd(a,b,c):
    assert a+b==c
@pytest.mark.parametrize("a,b,c",[("yas","cerdo","yascerdo"),("ijhur","kyir","ijhurkyi")])
def test_functionstr(a,b,c):
    assert a+b==c

