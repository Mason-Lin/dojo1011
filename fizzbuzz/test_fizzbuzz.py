"""
    http://codingdojo.org/kata/FizzBuzz/
"""
import pytest 
from fizzbuzz import result

def test_should_return_fizz():
    assert result(3) == "fizz"
    assert result(6) == "fizz"

def test_given_float_should_return_fizz():
    with pytest.raises(NotImplementedError):
        result(3.3)

def test_should_raise_execution_error():
    with pytest.raises(TypeError):
        result(None)

def test_should_return_number():
    assert result(1) == "1"
    assert result(2) == "2"

def test_should_return_buzz():
    assert result(5) == "buzz"
    assert result(10) == "buzz"

def test_should_return_fizzbuzz():
    assert result(15) == "fizzbuzz"
