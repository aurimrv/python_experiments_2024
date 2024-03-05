import pytest
from stack2 import Stack

def test_pop_method_mutant():
    # Create an empty stack
    stack = Stack()

    # Test the mutant code: pop should raise an exception with the original message
    with pytest.raises(Exception) as exception:
        stack.pop()
    assert str(exception.value) == "Stack is empty."
