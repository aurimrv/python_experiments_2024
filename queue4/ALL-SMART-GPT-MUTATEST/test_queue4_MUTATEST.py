import pytest
from queue4 import Node, DoubleLinkedList, Queue

def test_pop_non_empty_list():
    # Test popping from a non-empty list
    non_empty_list = DoubleLinkedList([42, 56, 73])

    popped_value = non_empty_list.pop()

    assert popped_value == 73
    assert non_empty_list.head.data == 56
    assert non_empty_list.head.prev is None
    assert non_empty_list.tail.data == 42
    assert non_empty_list.tail.next is None

def test_peek_empty_queue():
    # Test peeking from an empty queue
    empty_queue = Queue()

    assert empty_queue.peek() == None

def test_remove_head():
    # Test removing a value from the head of the list
    linked_list = DoubleLinkedList([1, 2, 3, 4])
    linked_list.remove(4)

    assert linked_list.head.data == 3
    assert linked_list.head.prev is None
    assert linked_list.tail.data == 1
    assert linked_list._repr() == [3, 2, 1]

def test_remove_tail():
    # Test removing a value from the tail of the list
    linked_list = DoubleLinkedList([1, 2, 3, 4])
    linked_list.remove(1)

    assert linked_list.head.data == 4
    assert linked_list.tail.next is None
    assert linked_list.tail.data == 2
    assert linked_list._repr() == [4, 3, 2]

def test_shift_repeated_shifts():
    # Test multiple consecutive shifts
    repeated_shifts_list = DoubleLinkedList([1, 2, 3, 4])

    shifted_value_1 = repeated_shifts_list.shift()
    shifted_value_2 = repeated_shifts_list.shift()
    shifted_value_3 = repeated_shifts_list.shift()

    assert shifted_value_1 == 1
    assert shifted_value_2 == 2
    assert shifted_value_3 == 3
    assert repeated_shifts_list.head.data == 4
    assert repeated_shifts_list.tail is not None

def test_shift_method_new_tail_next():
    # Test the shift method on a double-linked list
    dll = DoubleLinkedList([42, 56, 73])

    dll.shift()

    assert dll.tail.next is None
    assert dll._length == 2

def test_pop_one_item():
    # Test popping from a list with two items
    two_items_list = DoubleLinkedList([42, 56])

    popped_value = two_items_list.pop()

    assert popped_value == 56
    assert two_items_list.head.data == 42
    assert two_items_list.head.prev is None
    assert two_items_list.tail is not None
