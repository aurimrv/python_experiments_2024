#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue5/MIO/test_queue5.py.orig
import queue5 as module_0

def test_case_0():
    queue_0 = module_0.Queue()
    var_0 = queue_0.enqueue(queue_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'

def test_case_1():
    queue_0 = module_0.Queue()
    var_0 = queue_0.enqueue(queue_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'
    var_1 = queue_0.enqueue(queue_0)

def test_case_2():
    queue_0 = module_0.Queue()
    var_0 = queue_0.dequeue()

def test_case_3():
    queue_0 = module_0.Queue()
    var_0 = queue_0.enqueue(queue_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'
    var_1 = queue_0.dequeue()
    assert queue_0.head is None
    assert queue_0.tail is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue5.Queue'
    assert var_1.head is None
    assert var_1.tail is None

def test_case_4():
    queue_0 = module_0.Queue()
    var_0 = queue_0.enqueue(queue_0)
    assert f'{type(queue_0.head).__module__}.{type(queue_0.head).__qualname__}' == 'queue5.Node'
    assert f'{type(queue_0.tail).__module__}.{type(queue_0.tail).__qualname__}' == 'queue5.Node'
    var_1 = queue_0.enqueue(queue_0)
    var_2 = queue_0.dequeue()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'queue5.Queue'
    assert f'{type(var_2.head).__module__}.{type(var_2.head).__qualname__}' == 'queue5.Node'
    assert f'{type(var_2.tail).__module__}.{type(var_2.tail).__qualname__}' == 'queue5.Node'

def test_case_5():
    queue_0 = module_0.Queue()
