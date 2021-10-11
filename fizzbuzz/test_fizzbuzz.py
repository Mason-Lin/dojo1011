"""
    http://codingdojo.org/kata/FizzBuzz/
"""
from fizzbuzz import result

def test_should_return_fizz():
    assert result(3) == "fizz"
    assert result(6) == "fizz"

def test_should_return_number():
    assert result(1) == "1"
    assert result(2) == "2"

def test_should_return_buzz():
    assert result(5) == "buzz"
    assert result(10) == "buzz"
