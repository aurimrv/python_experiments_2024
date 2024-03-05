import pytest
from linkedList4 import LinkedList, Node

def test_remove():
    linked_list = LinkedList([10, 20, 30])
    linked_list.remove(10)

    assert linked_list.size() == 2
    assert linked_list.search(10) is None

def test_remove_head():
    linked_list = LinkedList([10, 20, 30])
    linked_list.remove(30)

    # Ensure that the head is removed, and the list is correct after removal
    assert linked_list.size() == 2
    assert linked_list.search(30) is None
    assert linked_list.head.data == 20
    assert linked_list.head.next.data == 10

def test_exception_pop():
    # Create an empty stack
    linked_list = LinkedList()

    # Test the mutant code: pop should raise an exception with the original message
    with pytest.raises(Exception) as exception:
        linked_list.pop()
    assert str(exception.value) == "Cannot pop from an empty list"
