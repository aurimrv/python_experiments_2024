import pytest
from stack5 import Stack, Node

def test_stack_pop():
    # Create a Stack with some initial data
    stack = Stack()
    stack.push(42)
    stack.push(23)

    # Test the original code: pop an element and check the return value
    popped_value = stack.pop()

    # Ensure that the popped value matches the last pushed value (Last In, First Out)
    assert popped_value == 23

def test_stack_is_empty():
    # Test the original code: create a Stack instance and check if it's initially empty
    stack = Stack()

    # Ensure that is_empty returns True for an empty stack
    assert stack.is_empty() is True

def test_stack_initialization_with_top():
    # Arrange
    value_to_set = 42

    # Act
    stack = Stack(top=value_to_set)

    # Assert
    assert stack.top == value_to_set
