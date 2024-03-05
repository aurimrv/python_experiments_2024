import pytest
from queue1 import Queue, QueueNode  

def test_init_method():
    with pytest.raises(TypeError):
        Queue.__init__()

def test_str_method():
    with pytest.raises(TypeError):
        Queue.__str__()

def test_init_method_other():
    with pytest.raises(TypeError):
        QueueNode.__init__(42)

def test_empty_queue_back_is_none():
    queue = Queue()

    # Verify that the 'back' attribute is None for an empty queue
    assert queue.back is None

def test_enqueue_two_elements_back_next():
    queue = Queue()

    # Enqueue the first element
    queue.enqueue(1)

    # Check that 'front' and 'back' point to the same node for the first element
    assert queue.front == queue.back

    # Enqueue the second element
    queue.enqueue(2)

    # Check that 'back' attribute of the first element now points to the second element
    assert queue.front.next == queue.back

    # Check that 'front' and 'back' point to different nodes for the second element
    assert queue.front != queue.back

    # Check that 'back.next' is None for the second element
    assert queue.back.next is None

    # Check the size of the queue after enqueuing two elements
    assert len(queue) == 2

def test_dequeue_front_next():
    queue = Queue()

    # Enqueue two elements
    queue.enqueue(1)
    queue.enqueue(2)

    # Dequeue the first element
    result = queue.dequeue()

    # Check that the result is the data of the first element
    assert result == 1

    # Check that 'front' attribute is now pointing to the second element
    assert queue.front.data == 2

    # Check that 'front.next' is None for the second element
    assert queue.front.next is None

    # Check the size of the queue after dequeueing one element
    assert len(queue) == 1

    # Dequeue the second element
    result = queue.dequeue()

    # Check that the result is the data of the second element
    assert result == 2

    # Check the size of the queue after dequeuing all elements
    assert len(queue) == 0

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

