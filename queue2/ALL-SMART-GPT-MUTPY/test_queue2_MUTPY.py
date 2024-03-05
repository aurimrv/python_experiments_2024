import pytest
from queue2 import LinkedList, QueueLinkedList, LinkedNode

def test_init_method():
    with pytest.raises(TypeError):
        QueueLinkedList.__init__()

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
    # Test popping from an empty queue
    empty_queue = QueueLinkedList()

    with pytest.raises(Exception, match="Queue is empty."):
        empty_queue.pop()

    # Ensure the queue remains empty
    assert empty_queue.head is None
    assert empty_queue.tail is None
    assert len(empty_queue) == 0

def test_pop_non_empty_queue():
    # Test popping elements from a non-empty queue
    queue = QueueLinkedList(1, 2, 3)

    # Pop elements and check if they were popped correctly
    popped_value = queue.pop()
    assert popped_value == 1
    assert len(queue) == 2
    assert list(queue) == [2, 3]
    # Linha adicionada manualmente
    assert queue.tail is not None

    popped_value = queue.pop()
    assert popped_value == 2
    assert len(queue) == 1
    assert list(queue) == [3]

    popped_value = queue.pop()
    assert popped_value == 3
    assert len(queue) == 0
    assert list(queue) == []

    # Attempt to pop from an empty queue
    with pytest.raises(Exception, match="Queue is empty."):
        queue.pop()

    # Ensure the queue remains empty after the attempted pop operation
    assert queue.head is None
    assert queue.tail is None
    assert len(queue) == 0

def test_linked_list_pop_exception():
    # Test pop method in LinkedList with an empty list
    ll = LinkedList()

    with pytest.raises(Exception, match="Linked list is empty."):
        ll.pop()

def test_linked_list_methods():
    # Create a linked list with initial values
    ll = LinkedList(1, 2, 3, 4)

    # Test __len__ method
    assert len(ll) == 4

    # Test __repr__ method
    assert repr(ll) == 'link:[4,3,2,1]'

    # Test __iter__ method
    assert list(ll) == [4, 3, 2, 1]

def test_remove_middle_element():
    # Create an instance of LinkedList with multiple items
    linked_list = LinkedList(10, 20, 30, 40, 50)

    # Remove an element in the middle (e.g., 30)
    linked_list.remove(30)

    # Verify the state after removal
    assert len(linked_list) == 4
    assert list(linked_list) == [50, 40, 20, 10]
