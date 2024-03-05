import pytest
from stack2 import Stack as module_0

def test_pop_method_mutant():
    # Create an empty stack
    stack = module_0()

    # Test the mutant code: pop should raise an exception for an empty stack
    with pytest.raises(Exception, match="Stack is empty."):
        stack.pop()
