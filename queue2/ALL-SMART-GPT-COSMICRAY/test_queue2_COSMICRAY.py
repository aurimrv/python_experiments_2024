import pytest
from queue2 import LinkedList, QueueLinkedList, LinkedNode

def test_check_infinite():
    # Create a linked list with a loop
    node1 = LinkedNode(1)
    node2 = LinkedNode(2)
    
    node1.next = node2
    node2.next = node1

    # Test checkInfinite method
    assert node1.checkInfinite() == True

def test_pop_multiple_items():
    # Create an instance of QueueLinkedList with multiple items
    queue = QueueLinkedList(10, 20, 30, 40)

    # Verify the initial state
    assert not queue.isEmpty()
    assert len(queue) == 4

    # Pop one item
    popped_value = queue.pop()

    # Verify the state after popping
    assert not queue.isEmpty()
    assert len(queue) == 3
    assert popped_value == 10
    assert queue.head.value == 20
    assert queue.tail.value == 40
