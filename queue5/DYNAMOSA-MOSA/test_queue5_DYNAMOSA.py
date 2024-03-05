#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue5/DYNAMOSA/test_queue5.py.orig
import pytest
import queue5 as module_0

def test_case_0():
    queue_0 = module_0.Queue()
    var_0 = queue_0.enqueue(queue_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'

def test_case_1():
    queue_0 = module_0.Queue()
    bool_0 = True
    var_0 = queue_0.enqueue(queue_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'
    queue_1 = module_0.Queue()
    queue_2 = module_0.Queue()
    node_0 = module_0.Node(bool_0)
    var_1 = queue_2.enqueue(queue_2)
    var_2 = queue_2.dequeue()
    assert queue_2.head is None
    assert queue_2.tail is None
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'queue5.Queue'
    assert var_2.head is None
    assert var_2.tail is None
    var_3 = queue_0.enqueue(bool_0)
    var_4 = var_2.dequeue()
    node_1 = module_0.Node(queue_2)
    var_5 = queue_2.enqueue(node_0)
    var_6 = var_2.enqueue(var_2)
    queue_3 = module_0.Queue()
    node_2 = module_0.Node(bool_0)

def test_case_2():
    queue_0 = module_0.Queue()
    var_0 = queue_0.dequeue()

def test_case_3():
    queue_0 = module_0.Queue()
    none_type_0 = None
    var_0 = queue_0.enqueue(none_type_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'
    var_1 = queue_0.dequeue()
    assert queue_0.head is None
    assert queue_0.tail is None

def test_case_4():
    bool_0 = False
    queue_0 = module_0.Queue()
    queue_1 = module_0.Queue()
    var_0 = queue_0.enqueue(bool_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'
    node_0 = module_0.Node(var_0)
    queue_2 = module_0.Queue()
    var_1 = queue_2.enqueue(queue_1)
    var_2 = queue_0.dequeue()
    assert var_2 is False
    assert queue_0.head is None
    assert queue_0.tail is None
    var_3 = queue_2.enqueue(queue_0)
    var_4 = queue_2.enqueue(queue_0)
    var_5 = queue_2.dequeue()
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'queue5.Queue'
    assert var_5.head is None
    assert var_5.tail is None
    var_6 = queue_2.dequeue()
    assert f'{type(var_6).__module__}.{type(var_6).__qualname__}' == 'queue5.Queue'
    assert var_6.head is None
    assert var_6.tail is None
    queue_3 = module_0.Queue()
    var_7 = queue_3.dequeue()
    var_8 = var_5.enqueue(var_4)
    var_9 = queue_2.dequeue()
    assert f'{type(var_9).__module__}.{type(var_9).__qualname__}' == 'queue5.Queue'
    assert var_9.head is None
    assert var_9.tail is None
    var_10 = var_5.dequeue()
    assert queue_1.tail is None
    assert var_5.tail is None
    var_11 = queue_2.enqueue(queue_0)
    var_12 = queue_1.dequeue()
    var_13 = queue_1.enqueue(bool_0)
    queue_4 = module_0.Queue()
