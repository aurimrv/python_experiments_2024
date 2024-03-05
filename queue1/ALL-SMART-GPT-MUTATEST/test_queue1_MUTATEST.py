import pytest
from queue1 import Queue, QueueNode 

def test_empty_queue_back_is_none():
    queue = Queue()

    # Verify that the 'back' attribute is None for an empty queue
    assert queue.back is None

def test_peek_empty_queue():
    # Create an empty queue
    queue = Queue()

    # Verify that peek returns None for an empty queue
    assert queue.peek() is None

def test_enqueue_multiple_elements():
    # Create an empty queue
    queue = Queue()

    # Enqueue multiple elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Verify the state after enqueuing multiple elements
    assert len(queue) == 3
    assert queue.front.data == 1
    assert queue.front.next.data == 2
    assert queue.back.data == 3
    assert queue.back.next is None

def test_clear_method():
    # Create a queue and enqueue some elements
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Call the clear method
    queue.clear()

    # Verify the state after calling clear
    assert len(queue) == 0
    assert queue.front is None
    assert queue.back is None

