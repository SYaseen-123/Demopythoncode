import first_test
def function_pytest_test(x):
    return x*10
def test_pytest_function():
    assert function_pytest_test(3)==30
    assert function_pytest_test(3)==40