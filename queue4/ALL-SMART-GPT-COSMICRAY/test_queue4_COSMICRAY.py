import pytest
from queue4 import Node, DoubleLinkedList, Queue

def test_double_linked_list_append_shift():
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)

    shifted_value = dll.shift()
    assert shifted_value == 3
    assert dll.tail.data == 2
    assert dll._repr() == [1, 2]

def test_pop_two_elements_list():
    # Test popping from a list with two elements
    two_elements_list = DoubleLinkedList([42, 56])

    popped_value = two_elements_list.pop()

    assert popped_value == 56
    assert two_elements_list.head.data == 42
    assert two_elements_list.tail.data == 42

def test_remove():
    # Test removing a value from the list
    linked_list = DoubleLinkedList([1, 2, 3, 4])
    linked_list.remove(3)

    assert linked_list.head.data == 4
    assert linked_list.tail.data == 1
    assert linked_list._length == 3
    assert linked_list._repr() == [4, 2, 1]

