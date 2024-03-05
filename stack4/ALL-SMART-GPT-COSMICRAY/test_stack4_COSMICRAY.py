import pytest
from stack4 import Stack, LinkedList

def test_remove_method_length():
    # Test the remove method and assert the updated length.

    # Create a linked list with some initial values.
    linked_list = LinkedList([1, 'apple', 3.14, 'banana', 42])

    # Use the remove method to remove a node (e.g., 'banana').
    linked_list.remove('banana')

    # Assertion: Check the updated length after removal.
    assert linked_list.size() == 4

def test_pop_method_length():
    # Test the pop method and assert the updated length.

    # Create a linked list with some initial values.
    linked_list = LinkedList([1, 'apple', 3.14, 'banana', 42])

    # Use the pop method to remove an element (e.g., pop the last element).
    linked_list.pop()

    # Assertion: Check the updated length after the pop operation.
    assert linked_list.size() == 4

def test_remove_method_remove_head():
    # Test the remove method by removing the head of the list.

    # Create a linked list with some initial values.
    linked_list = LinkedList([1, 'apple', 3.14, 'banana', 42])

    # Use the remove method to remove the head of the list (1).
    linked_list.remove(42)

    # Check the updated length after removal.
    assert linked_list.size() == 4
