import pytest
from queue4 import Node, DoubleLinkedList, Queue

def test_pop_empty_list():
    empty_list = DoubleLinkedList()

    with pytest.raises(Exception) as exception:
        empty_list.pop()
    assert str(exception.value) == "Cannot pop from an empty list."

def test_shift_empty_list():
    empty_list = DoubleLinkedList()

    with pytest.raises(Exception) as exception:
        empty_list.shift()
    assert str(exception.value) == "Cannot shift from an empty list."

def test_remove_item_not_in_list():
    # Test removing an item that is not in the list
    list_with_items = DoubleLinkedList([42, 56, 73])

    with pytest.raises(ValueError) as exc_info:
        list_with_items.remove(99)

    assert str(exc_info.value) == '99 is not in the list'

def test_pop_middle_item():
    # Test popping the middle item from a 3-element queue
    three_element_list = DoubleLinkedList([42, 56, 73])

    popped_value = three_element_list.pop()

    assert popped_value == 73
    assert three_element_list.head.prev is None
    assert three_element_list._repr() == [56, 42]

def test_remove_method():
    dll = DoubleLinkedList([42, 56, 73])

    dll.remove(56)

    assert dll._length == 2
    assert dll.tail.next is None

def test_shift_method_new_tail_next():
    # Test the shift method on a double-linked list
    dll = DoubleLinkedList([42, 56, 73])

    dll.shift()

    assert dll.tail.next is None
    assert dll._length == 2

def test_pop_from_two_element_list():
    # Test popping from a double-linked list with two elements
    dll = DoubleLinkedList([42, 56])

    dll.pop()

    assert dll.tail is not None

def test_shift_method_length():
    # Test the shift method on a double-linked list
    dll = DoubleLinkedList([42, 56, 73])

    dll.shift()

    assert dll._length == 2
