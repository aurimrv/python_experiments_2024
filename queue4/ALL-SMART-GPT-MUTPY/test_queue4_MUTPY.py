import pytest
from queue4 import Node, DoubleLinkedList, Queue

def test_double_linked_list_append_shift():
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)

    shifted_value = dll.shift()
    assert shifted_value == 3
    assert dll._repr() == [1, 2]

def test_queue_peek():
    queue = Queue([1, 2, 3])
    assert queue.peek() == 3

    queue.dequeue()
    assert queue.peek() == 2

def test_queue_size_empty():
    empty_queue = Queue()
    assert empty_queue.size() == 0

    empty_queue.enqueue(1)
    empty_queue.dequeue()
    assert empty_queue.size() == 0

def test_shift_empty_list():
    # Test shifting from an empty list
    empty_list = DoubleLinkedList()

    with pytest.raises(IndexError, match="Cannot shift from an empty list."):
        empty_list.shift()

    # Ensure the list remains empty
    assert empty_list.head is None
    assert empty_list.tail is None

def test_shift_single_element_list():
    # Test shifting from a list with a single element
    single_element_list = DoubleLinkedList([1])

    shifted_value = single_element_list.shift()
    assert shifted_value == 1
    assert single_element_list.tail is None

def test_shift_multiple_elements_list():
    # Test shifting from a list with multiple elements
    multiple_elements_list = DoubleLinkedList([1, 2, 3])

    shifted_value = multiple_elements_list.shift()
    assert shifted_value == 1

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

def test_remove_head():
    # Test removing a value from the head of the list
    linked_list = DoubleLinkedList([1, 2, 3, 4])
    linked_list.remove(4)

    assert linked_list.head.data == 3
    assert linked_list.tail.data == 1
    assert linked_list._repr() == [3, 2, 1]

def test_init_method():
    with pytest.raises(TypeError):
        Queue.__init__()

def test_pop_empty_list():
    # Test popping from an empty list
    empty_list = DoubleLinkedList()

    with pytest.raises(IndexError, match="Cannot pop from an empty list."):
        empty_list.pop()

def test_remove_value_not_in_list():
    # Test removing a value not in the list
    linked_list = DoubleLinkedList([1, 2, 3, 4])

    with pytest.raises(ValueError, match="5 is not in the list"):
        linked_list.remove(5)

def test_pop_two_elements_list():
    # Test popping from a list with two elements
    two_elements_list = DoubleLinkedList([42, 56])

    popped_value = two_elements_list.pop()

    assert popped_value == 56
    assert two_elements_list.head.data == 42
    assert two_elements_list.tail.data == 42

def test_pop_multiple_elements():
    # Test popping from a list with multiple elements
    multiple_elements_list = DoubleLinkedList([42, 56, 73])

    popped_value = multiple_elements_list.pop()

    assert popped_value == 73
    assert multiple_elements_list.head.data == 56
    assert multiple_elements_list.head.prev is None
    assert multiple_elements_list.tail.data == 42
    assert multiple_elements_list.tail.next is None
