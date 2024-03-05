#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue1/DYNAMOSA/test_queue1.py.orig
import pytest
import queue1 as module_0

def test_case_0():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1

def test_case_1():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    with pytest.raises(ValueError):
        queue_0.dequeue()

def test_case_2():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.peek()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0

def test_case_3():
    str_0 = 'I*So4'
    queue_node_0 = module_0.QueueNode(str_0)
    dict_0 = {}
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(dict_0)
    assert len(queue_0) == 1
    var_1 = queue_0.peek()
    var_2 = queue_0.dequeue()
    assert len(queue_0) == 0

def test_case_4():
    none_type_0 = None
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()

def test_case_5():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    var_1 = queue_0.clear()

def test_case_6():
    dict_0 = {}
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(dict_0)
    assert len(queue_0) == 1
    var_1 = queue_0.dequeue()
    assert len(queue_0) == 0

def test_case_7():
    str_0 = '\\=BToYP3(\rYl?ol$]='
    queue_node_0 = module_0.QueueNode(str_0)
    dict_0 = {}
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(dict_0)
    assert len(queue_0) == 1
    var_1 = queue_0.enqueue(var_0)
    assert len(queue_0) == 2
