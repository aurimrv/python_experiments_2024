import pytest
from stack5 import Node  # Replace 'stack5' with the actual module name
from stack5 import Stack 
import builtins as module_1

def test_peek_method():
    # Create a stack with some data
    stack = Stack()
    stack.push(42)

    # Test the original code: peek should return the top data
    assert stack.peek() == 42

def test_is_empty_method():
    # Test the original code: is_empty should return True for an empty stack
    stack_empty = Stack()
    assert stack_empty.is_empty() is True

    # Test the original code: is_empty should return False for a non-empty stack
    stack_non_empty = Stack()
    stack_non_empty.push(42)
    assert stack_non_empty.is_empty() is False

def test_call_init():
    with pytest.raises(TypeError) as typeerror:
        node = Node.__init__(5)
