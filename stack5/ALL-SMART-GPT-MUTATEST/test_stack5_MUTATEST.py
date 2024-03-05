import pytest
from stack5 import Stack
from stack5 import Node
import builtins as module_1

def test_pop_method_mutant():
    # Create an empty stack
    stack = Stack()

    # Test the mutant code: pop should return None for an empty stack
    assert stack.pop() is None

def test_peek_method_original():
    # Create an empty stack
    stack = Stack()

    # Test the original code: peek should return None for an empty stack
    assert stack.peek() is None

def test_is_empty_method_mutant():
    # Create an empty stack
    stack = Stack()

    # Test the mutant code: is_empty should return True for an empty stack
    assert stack.is_empty() is True

def test_node_original():
    # Create an instance of Node with some data
    node = Node(42)

    # Test the original code: next should be None
    assert node.next is None
