import pytest
from queue2 import LinkedList, QueueLinkedList, LinkedNode

def test_check_infinite():
    # Create a linked list with an infinite loop
    node1 = LinkedNode(1)
    node2 = LinkedNode(2)
    node1.next = node2
    node2.next = node1

    assert node1.checkInfinite()

def test_pop_method_mutant1():
    # Create an empty stack
    ll = LinkedList()

    # Test the mutant code: pop should raise an exception with the original message
    with pytest.raises(Exception) as exception:
        ll.pop()
    assert str(exception.value) == "Linked list is empty."

def test_pop_method_mutant2():
    # Create an empty stack
    qll = QueueLinkedList()

    # Test the mutant code: pop should raise an exception with the original message
    with pytest.raises(Exception) as exception:
        qll.pop()
    assert str(exception.value) == "Queue is empty."

    assert qll.head is None
    assert qll.tail is None
    assert len(qll) == 0

def test_empty_queue():
    # Create an instance of an empty QueueLinkedList
    queue = QueueLinkedList()

    # Test if the queue is empty
    assert queue.head is None
    assert queue.tail is None
    assert queue.isEmpty()
    assert len(queue) == 0

def test_pop_single_item():
    # Create an instance of QueueLinkedList with a single item
    queue = QueueLinkedList(42)

    # Verify the initial state
    assert not queue.isEmpty()
    assert len(queue) == 1

    # Pop the single item
    popped_value = queue.pop()

    # Verify the state after popping
    assert queue.isEmpty()
    assert len(queue) == 0
    assert popped_value == 42
    assert queue.head is None
    assert queue.tail is None

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

def test_remove_middle_element():
    # Create an instance of LinkedList with multiple items
    linked_list = LinkedList(10, 20, 30, 40, 50)

    # Remove an element in the middle (e.g., 30)
    linked_list.remove(30)

    # Verify the state after removal
    assert len(linked_list) == 4
    assert list(linked_list) == [50, 40, 20, 10]
