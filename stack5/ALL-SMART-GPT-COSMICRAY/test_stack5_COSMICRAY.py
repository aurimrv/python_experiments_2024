import pytest
from stack5 import Stack

def test_stack_is_empty():
    # Test the original code: create a Stack instance and check if it's initially empty
    stack = Stack()

    # Ensure that is_empty returns True for an empty stack
    assert stack.is_empty() is True

