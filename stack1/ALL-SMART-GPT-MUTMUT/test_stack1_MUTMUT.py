import pytest
from stack1 import Stack, StackNode, check_parenthesis, postfix_eval

def test_postfix_eval_add():
    assert postfix_eval("2 3 +") == 5

def test_postfix_eval_multiplication():
    result = postfix_eval("3 4 *")
    assert result == 12

def test_postfix_eval_general_division():
    result = postfix_eval("9 2 /")
    assert result == 4.5

def test_postfix_eval_modulus():
    result = postfix_eval("10 3 %")
    assert result == 1

def test_postfix_eval_exponentiation():
    result = postfix_eval("2 3 ^")
    assert result == 8

def test_postfix_eval_subtraction():
    result = postfix_eval("7 3 -")
    assert result == 4

def test_postfix_eval_raises_value_error_for_excessive_operands():
    with pytest.raises(ValueError):
        postfix_eval("1 4")
