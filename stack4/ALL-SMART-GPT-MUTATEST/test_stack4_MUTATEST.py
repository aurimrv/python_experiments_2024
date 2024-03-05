import pytest
from stack4 import Node, Stack, LinkedList

def test_node_next_attribute():
    # Test that the 'next' attribute is set correctly in the original code.
    data_value = "test_data"
    
    # Original code should work with None as the default value for next_node.
    original_node = Node(data_value)
    assert original_node.data == data_value
    assert original_node.next is None

def test_remove_method_length_decrement():
    # Test if the length is decremented correctly in the LinkedList's remove method.

    # Create a linked list with some initial values.
    linked_list = LinkedList([1, 'apple', 3.14, 'banana', 42])

    # Remove a node from the linked list.
    linked_list.remove('banana')

    # Check if the length is decremented by 1 after removal.
    assert linked_list.size() == 4

def test_pop_method_length_decrement():
    # Test if the length is decremented correctly in the LinkedList's pop method.

    # Create a linked list with some initial values.
    linked_list = LinkedList([1, 'apple', 3.14, 'banana', 42])

    # Check the initial length of the linked list.
    initial_length = linked_list.size()

    # Perform a pop operation.
    popped_value = linked_list.pop()

    # Check if the popped value matches the expected value.
    assert popped_value == 42

    # Check if the length is decremented by 1 after the pop operation.
    assert linked_list.size() == initial_length - 1

def test_remove_method_length_decrement():
    # Test if the length is decremented correctly in the LinkedList's remove method.

    # Create a linked list with some initial values.
    linked_list = LinkedList([1, 'apple', 3.14, 'banana', 42])

    # Check the initial length of the linked list.
    initial_length = linked_list.size()

    # Remove a node using the remove method.
    linked_list.remove('banana')

    # Check if the length is decremented by 1 after the removal.
    assert linked_list.size() == initial_length - 1

def test_remove_method_length_decrement1():
    # Test if the length is decremented correctly in the LinkedList's remove method.

    # Create a linked list with some initial values.
    linked_list = LinkedList([1, 'apple', 3.14, 'banana', 42])

    # Check the initial length of the linked list.
    initial_length = linked_list.size()

    # Remove a node using the remove method.
    linked_list.remove(42)

    # Check if the length is decremented by 1 after the removal.
    assert linked_list.size() == initial_length - 1


def test_search_method():
    # Test if the search method returns the correct node in the LinkedList.

    # Create a linked list with some initial values.
    linked_list = LinkedList([1, 'apple', 3.14, 'banana', 42])

    # Search for a value in the linked list.
    found_node = linked_list.search('banana')

    # Check if the found node contains the expected value.
    assert found_node.data == 'banana'

def test_empty_stack_size():
    empty_stack = Stack()

    assert empty_stack._stack.size() == 0
