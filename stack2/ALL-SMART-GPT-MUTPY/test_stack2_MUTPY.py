import pytest
import inspect
from stack2 import Stack

def test_pop_method_mutant():
    # Create an empty stack
    stack = Stack()

    # Test the mutant code: pop should raise an exception with the original message
    with pytest.raises(Exception, match="Stack is empty."):
        stack.pop()

def test_call_init():
    with pytest.raises(TypeError) as typeerror:
        stack = Stack.__init__()
