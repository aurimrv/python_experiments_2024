import pytest
from queue5 import Queue 

def test_enqueue_empty_queue():
    queue = Queue()

    # Enqueue an element to an empty queue
    queue.enqueue(42)

    # Check that head and tail are not None after enqueueing
    assert queue.head is not None
    assert queue.tail is not None

    # Check that head and tail point to the same node
    assert queue.head == queue.tail

    # Check the data in the enqueued node
    assert queue.head.data == 42
    assert queue.tail.data == 42

    # Check that the next pointer of the node is None
    assert queue.head.next is None
    assert queue.tail.next is None

    # Additional check: Dequeue should return the enqueued element
    assert queue.dequeue() == 42

    # After dequeue, head and tail should be None again
    assert queue.head is None
    assert queue.tail is None

    # Dequeue from an empty queue should return None
    assert queue.dequeue() is None
