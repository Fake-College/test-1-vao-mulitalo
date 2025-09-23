import pytest
from common_setup import run_test

def test_my_name():

    # the first parameter is the name of the test file in /tests
    # the second parameter is the name of the test in autograding.json
    # the third parameter is the error message to display if the test fails
    run_test("my_name", "Check for name output", "The program doesn't return your name")

if __name__ == '__main__':
    pytest.main()