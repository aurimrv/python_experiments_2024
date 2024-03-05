import pytest
from linkedList4 import LinkedList, Node

def test_exception_pop():
    # Create an empty stack
    linked_list = LinkedList()

    # Test the mutant code: pop should raise an exception with the original message
    with pytest.raises(Exception) as exception:
        linked_list.pop()
    assert str(exception.value) == "Cannot pop from an empty list"

def test_remove_head():
    linked_list = LinkedList([10, 20, 30])
    linked_list.remove(30)

    # Ensure that the head is removed, and the list is correct after removal
    assert linked_list.size() == 2
    assert linked_list.search(30) is None
    assert linked_list.head.data == 20
    assert linked_list.head.next.data == 10

def test_remove_and_display():
    linked_list = LinkedList([10, 20, 30])
    linked_list.remove(20)

    assert linked_list.size() == 2
    assert linked_list.search(20) is None

    # Verify the state of the linked list using the display method
    display_string = linked_list.display()
    assert display_string == "(30, 10)"

def test_pop_and_verify_head():
    linked_list = LinkedList([10, 20, 30])
    popped_value = linked_list.pop()

    # Ensure that the popped value is correct and verify the new head of the linked list
    assert popped_value == 30
    assert linked_list.size() == 2
    assert linked_list.head.data == 20
    assert linked_list.head.next.data == 10
