import pytest
from stack4 import Stack, LinkedList

def test_pop_exception_message():
    # Test if the exception message matches the expected value.

    stack = Stack()

    # Attempt to pop from an empty stack with the original exception message.
    with pytest.raises(IndexError) as exc_info:
        stack.pop()

    # Check if the exception message matches the original message.
    assert str(exc_info.value) == 'Cannot pop from an empty list'

    # Attempt to pop from an empty stack with the altered exception message.
    with pytest.raises(IndexError) as exc_info:
        stack.pop()

    # Check if the exception message matches the altered message (should fail).
    with pytest.raises(AssertionError):
        assert str(exc_info.value) == 'XXCannot pop from an empty listXX'

def test_pop_method():
    # Test the pop method.

    # Create a linked list with some initial values.
    linked_list = LinkedList([1, 'apple', 3.14, 'banana', 42])

    # Check the initial length of the linked list.
    assert linked_list.size() == 5

    # Perform pop operations and check the returned values.
    assert linked_list.pop() == 42
    assert linked_list.pop() == 'banana'
    assert linked_list.pop() == 3.14

    # Check the updated length after pops.
    assert linked_list.size() == 2

    # Perform more pops and check the returned values.
    assert linked_list.pop() == 'apple'
    assert linked_list.pop() == 1

    # Check the length after all pops.
    assert linked_list.size() == 0

    # Attempt to pop from an empty list (should raise IndexError).
    with pytest.raises(IndexError, match='Cannot pop from an empty list'):
        linked_list.pop()

    # Check that the length remains 0 after attempting to pop from an empty list.
    assert linked_list.size() == 0

def test_search_method():
    # Test the search method.

    # Create a linked list with some initial values.
    linked_list = LinkedList([1, 'apple', 3.14, 'banana', 42])

    # Test searching for existing values.
    assert linked_list.search('apple').data == 'apple'
    assert linked_list.search(42).data == 42

    # Test searching for a non-existing value.
    assert linked_list.search('orange') is None

    # Test searching in an empty list.
    empty_list = LinkedList()
    assert empty_list.search('apple') is None

def test_remove_from_linked_list():
    data = ['apple', 'banana', 'cherry', 'date']
    linked_list = LinkedList(data)

    # Test initial state
    assert linked_list.size() == 4
    assert linked_list.display() == "(date, cherry, banana, apple)"

    # Remove the 3rd element ('cherry')
    linked_list.remove('cherry')

    # Test after removal
    assert linked_list.size() == 3
    assert linked_list.display() == "(date, banana, apple)"

def test_remove_head_from_linked_list():
    data = ['apple', 'banana', 'cherry', 'date']
    linked_list = LinkedList(data)

    # Test initial state
    assert linked_list.size() == 4
    assert linked_list.display() == "(date, cherry, banana, apple)"

    # Remove the head element ('date')
    linked_list.remove('date')

    # Test after removal
    assert linked_list.size() == 3
    assert linked_list.display() == "(cherry, banana, apple)"
