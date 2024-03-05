import pytest
from linkedList2 import LinkedNode, LinkedList

def test_check_infinite_with_loop():
    # Create a linked list with an infinite loop
    node1 = LinkedNode(1)
    node2 = LinkedNode(2)
    node1.next = node2
    node2.next = node1

    assert node1.checkInfinite()

def test_check_infinite_with_loop1():
    # Create a linked list with an infinite loop
    node1 = LinkedNode(1)
    node2 = LinkedNode(2)
    node1.next = node2
    node2.next = node2

    assert node1.checkInfinite()

def test_pop_empty_queue():
    # Test popping from an empty list
    empty_list = LinkedList()

    with pytest.raises(Exception) as exception:
         empty_list.pop()
    assert str(exception.value) == "Linked list is empty."

def test_remove_middle_element():
    # Create an instance of LinkedList with multiple items
    linked_list = LinkedList(10, 20, 30, 40, 50)

    # Remove an element in the middle (e.g., 30)
    linked_list.remove(30)

    # Verify the state after removal
    assert len(linked_list) == 4
    assert list(linked_list) == [50, 40, 20, 10]
