#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue1/RANDOM/test_queue1.py
import pytest
import queue1 as module_0

def test_case_0():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)

def test_case_1():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0

def test_case_2():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0

def test_case_3():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1

def test_case_4():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0

def test_case_5():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    var_2 = queue_2.enqueue(none_type_2)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_node_4 = module_0.QueueNode(none_type_1)

def test_case_6():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)

def test_case_7():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    var_3 = queue_0.__str__()

def test_case_8():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'

def test_case_9():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0

def test_case_10():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_1 = queue_1.enqueue(none_type_1)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_node_3 = module_0.QueueNode(queue_0)
    assert len(queue_node_3.data) == 0

def test_case_11():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0

def test_case_12():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_1 = queue_3.__len__()
    assert var_1 == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    var_4 = var_0.__str__()
    assert var_4 == '0'

def test_case_13():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_2 = queue_3.enqueue(none_type_1)
    assert len(queue_3) == 1
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_3 = queue_5.__len__()
    assert var_3 == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    none_type_5 = None
    queue_node_5 = module_0.QueueNode(none_type_5)
    tuple_0 = ()
    queue_node_6 = module_0.QueueNode(tuple_0)
    var_6 = queue_3.clear()
    assert len(queue_3) == 0

def test_case_14():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_1 = queue_1.enqueue(none_type_1)
    assert len(queue_1) == 1
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = queue_0.__str__()

def test_case_15():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()

def test_case_16():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_0.enqueue(var_0)
    assert len(queue_0) == 1

def test_case_17():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__str__()
    var_4 = queue_3.peek()

def test_case_18():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__str__()
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_6 = module_0.QueueNode(tuple_1)
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_4 = queue_6.__len__()
    assert var_4 == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_5.__len__()
    assert var_7 == 0

def test_case_19():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    tuple_1 = ()
    queue_node_3 = module_0.QueueNode(tuple_1)
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    var_2 = queue_3.enqueue(none_type_2)
    assert len(queue_3) == 1
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = queue_0.enqueue(tuple_0)
    assert len(queue_0) == 1

def test_case_20():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0

def test_case_21():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()

def test_case_22():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    var_3 = queue_3.clear()
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    tuple_1 = ()
    queue_node_7 = module_0.QueueNode(tuple_1)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.__str__()
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0

def test_case_23():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    var_5 = var_4.__len__()

def test_case_24():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()

def test_case_25():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__str__()
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    var_6 = queue_5.enqueue(none_type_5)
    assert len(queue_5) == 1
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_7 = queue_9.__len__()
    assert var_7 == 0
    var_8 = queue_9.__len__()
    assert var_8 == 0
    var_9 = var_8.__str__()
    assert var_9 == '0'
    var_10 = queue_8.peek()
    var_11 = queue_6.__str__()

def test_case_26():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__str__()
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = var_0.__str__()
    assert var_5 == '0'

def test_case_27():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_6 = module_0.QueueNode(tuple_1)
    var_4 = queue_4.clear()
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_6 = queue_8.__len__()
    assert var_6 == 0
    var_7 = queue_8.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    var_9 = queue_7.peek()
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_10 = queue_10.__len__()
    assert var_10 == 0
    var_11 = queue_10.__len__()
    assert var_11 == 0
    var_12 = var_11.__str__()
    assert var_12 == '0'
    none_type_8 = None
    queue_node_10 = module_0.QueueNode(none_type_8)
    tuple_2 = ()
    queue_node_11 = module_0.QueueNode(tuple_2)
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0

def test_case_28():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    var_5 = queue_2.peek()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    var_7 = queue_5.enqueue(none_type_4)
    assert len(queue_5) == 1
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    none_type_8 = None
    queue_node_10 = module_0.QueueNode(none_type_8)
    tuple_2 = ()
    queue_node_11 = module_0.QueueNode(tuple_2)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__str__()
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_9 = None
    queue_node_12 = module_0.QueueNode(none_type_9)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_10 = queue_10.__len__()
    assert var_10 == 0
    var_11 = queue_10.__len__()
    assert var_11 == 0
    var_12 = var_11.__str__()
    assert var_12 == '0'
    queue_node_13 = module_0.QueueNode(none_type_8)

def test_case_29():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    var_3 = queue_3.enqueue(none_type_3)
    assert len(queue_3) == 1
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_node_8 = module_0.QueueNode(none_type_1)

def test_case_30():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    var_8 = queue_5.peek()
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0

def test_case_31():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__str__()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    var_3 = queue_3.enqueue(none_type_2)
    assert len(queue_3) == 1
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_4 = queue_6.__len__()
    assert var_4 == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_5.peek()
    none_type_6 = None
    queue_node_7 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_8 = module_0.QueueNode(tuple_1)
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__len__()
    assert var_8 == 0
    none_type_8 = None
    queue_node_10 = module_0.QueueNode(none_type_8)
    tuple_2 = ()
    queue_node_11 = module_0.QueueNode(tuple_2)
    var_9 = queue_7.clear()
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_9 = None
    queue_node_12 = module_0.QueueNode(none_type_9)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_10 = queue_10.__len__()
    assert var_10 == 0
    var_11 = queue_10.__len__()
    assert var_11 == 0
    var_12 = var_11.__str__()
    assert var_12 == '0'
    var_13 = queue_3.peek()

def test_case_32():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_2 = queue_1.__str__()
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    tuple_2 = ()
    queue_node_6 = module_0.QueueNode(tuple_2)
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_4.peek()
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__len__()
    assert var_8 == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    var_10 = var_9.__str__()
    assert var_10 == '0'
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_11 = queue_9.__len__()
    assert var_11 == 0
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    none_type_8 = None
    queue_node_11 = module_0.QueueNode(none_type_8)
    var_12 = queue_10.enqueue(none_type_7)
    assert len(queue_10) == 1
    none_type_9 = None
    queue_node_12 = module_0.QueueNode(none_type_9)
    queue_node_13 = module_0.QueueNode(queue_node_6)

def test_case_33():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = queue_1.__str__()

def test_case_34():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_2 = queue_1.__len__()
    assert var_2 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    var_3 = queue_2.enqueue(none_type_4)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_4.peek()
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    tuple_2 = ()
    queue_node_10 = module_0.QueueNode(tuple_2)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__str__()
    var_9 = queue_3.clear()

def test_case_35():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_1.clear()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_0.__str__()
    assert var_3 == '0'

def test_case_36():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.clear()

def test_case_37():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    var_2 = queue_2.enqueue(none_type_2)
    assert len(queue_2) == 1
    float_0 = 484.374
    queue_node_5 = module_0.QueueNode(float_0)

def test_case_38():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    var_5 = queue_2.peek()
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    float_0 = -3532.9
    queue_node_6 = module_0.QueueNode(float_0)

def test_case_39():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_2 = queue_3.enqueue(none_type_1)
    assert len(queue_3) == 1
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_6 = module_0.QueueNode(tuple_1)
    var_4 = queue_4.clear()
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0

def test_case_40():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_0.enqueue(none_type_0)
    assert len(queue_0) == 1

def test_case_41():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    var_3 = queue_2.clear()
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_4.peek()
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0

def test_case_42():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)

def test_case_43():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    var_6 = queue_3.peek()
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_7 = queue_5.__len__()
    assert var_7 == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    var_8 = queue_6.enqueue(none_type_3)
    assert len(queue_6) == 1
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    tuple_0 = ()
    queue_node_7 = module_0.QueueNode(tuple_0)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__str__()
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_9 = module_0.QueueNode(tuple_1)
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_10 = queue_9.__len__()
    assert var_10 == 0
    none_type_8 = None
    queue_node_11 = module_0.QueueNode(none_type_8)
    tuple_2 = ()
    queue_node_12 = module_0.QueueNode(tuple_2)
    var_11 = queue_9.clear()
    var_12 = queue_7.peek()

def test_case_44():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_5 = queue_4.enqueue(none_type_1)
    assert len(queue_4) == 1
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_6 = module_0.QueueNode(tuple_0)
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    tuple_1 = ()
    queue_node_10 = module_0.QueueNode(tuple_1)
    var_10 = queue_7.clear()
    none_type_8 = None
    queue_node_11 = module_0.QueueNode(none_type_8)
    tuple_2 = ()
    queue_node_12 = module_0.QueueNode(tuple_2)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_11 = queue_8.__str__()
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_9 = None
    queue_node_13 = module_0.QueueNode(none_type_9)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_12 = queue_10.__len__()
    assert var_12 == 0
    var_13 = queue_2.enqueue(queue_node_10)
    assert len(queue_2) == 1

def test_case_45():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    none_type_0 = None
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    var_1 = queue_1.clear()
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__str__()
    queue_node_6 = module_0.QueueNode(var_0)
    assert queue_node_6.data == 0

def test_case_46():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    var_5 = queue_2.peek()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_6 = module_0.QueueNode(tuple_1)
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    str_0 = 'a,~'
    queue_node_8 = module_0.QueueNode(str_0)
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_7 = queue_5.__len__()
    assert var_7 == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    var_8 = queue_6.enqueue(none_type_6)
    assert len(queue_6) == 1
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_8 = None
    queue_node_11 = module_0.QueueNode(none_type_8)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_9 = queue_9.__len__()
    assert var_9 == 0
    var_10 = queue_9.__len__()
    assert var_10 == 0
    var_11 = var_10.__str__()
    assert var_11 == '0'
    none_type_9 = None
    queue_node_12 = module_0.QueueNode(none_type_9)
    tuple_2 = ()
    queue_node_13 = module_0.QueueNode(tuple_2)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_12 = queue_10.__str__()
    var_13 = queue_4.__len__()
    assert var_13 == 0

def test_case_47():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    var_4 = queue_0.clear()

def test_case_48():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    var_3 = queue_3.enqueue(none_type_2)
    assert len(queue_3) == 1
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_6 = None
    queue_node_7 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0

def test_case_49():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_0 = queue_3.__len__()
    assert var_0 == 0
    var_1 = queue_3.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_2.peek()
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__str__()
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__len__()
    assert var_8 == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_6 = None
    queue_node_7 = module_0.QueueNode(none_type_6)
    var_10 = queue_9.enqueue(none_type_5)
    assert len(queue_9) == 1
    str_0 = 'a,~'
    queue_node_8 = module_0.QueueNode(str_0)
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    tuple_1 = ()
    queue_node_10 = module_0.QueueNode(tuple_1)
    queue_node_11 = module_0.QueueNode(none_type_4)

def test_case_50():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    var_2 = queue_1.clear()
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    var_5 = queue_4.enqueue(none_type_4)
    assert len(queue_4) == 1
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    tuple_2 = ()
    queue_node_9 = module_0.QueueNode(tuple_2)
    str_0 = 'a,~'
    queue_node_10 = module_0.QueueNode(str_0)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_8 = None
    queue_node_12 = module_0.QueueNode(none_type_8)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_9 = queue_10.__len__()
    assert var_9 == 0
    var_10 = queue_10.__len__()
    assert var_10 == 0
    var_11 = var_10.__str__()
    assert var_11 == '0'
    var_12 = queue_9.peek()
    none_type_9 = None
    queue_node_13 = module_0.QueueNode(none_type_9)
    var_13 = var_2.__str__()

def test_case_51():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    str_0 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_7 = module_0.QueueNode(tuple_1)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__str__()
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    var_7 = queue_7.enqueue(none_type_5)
    assert len(queue_7) == 1
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_8 = queue_9.__len__()
    assert var_8 == 0
    var_9 = queue_9.__len__()
    assert var_9 == 0
    var_10 = var_9.__str__()
    assert var_10 == '0'
    none_type_8 = None
    queue_node_11 = module_0.QueueNode(none_type_8)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_11 = queue_10.__len__()
    assert var_11 == 0
    none_type_9 = None
    queue_node_12 = module_0.QueueNode(none_type_9)
    tuple_2 = ()
    queue_node_13 = module_0.QueueNode(tuple_2)
    var_12 = queue_10.clear()
    bool_0 = True
    var_13 = queue_9.enqueue(bool_0)
    assert len(queue_9) == 1

def test_case_52():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    list_0 = [none_type_1, queue_3]
    var_5 = queue_3.enqueue(list_0)
    assert len(queue_3) == 1

def test_case_53():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__str__()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    var_3 = queue_3.enqueue(none_type_4)
    assert len(queue_3) == 1
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    tuple_2 = ()
    queue_node_10 = module_0.QueueNode(tuple_2)
    var_5 = queue_4.clear()
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_8 = None
    queue_node_11 = module_0.QueueNode(none_type_8)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_6 = queue_8.__len__()
    assert var_6 == 0
    var_7 = queue_8.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    var_9 = queue_7.peek()
    var_10 = queue_5.clear()

def test_case_54():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)

def test_case_55():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_1 = queue_1.enqueue(none_type_1)
    assert len(queue_1) == 1
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__str__()
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    str_0 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_0)
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    queue_node_9 = module_0.QueueNode(none_type_5)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_6 = None
    queue_node_10 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_8 = None
    queue_node_12 = module_0.QueueNode(none_type_8)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_8 = queue_9.__len__()
    assert var_8 == 0
    var_9 = queue_9.__len__()
    assert var_9 == 0
    var_10 = var_9.__str__()
    assert var_10 == '0'
    var_11 = queue_8.peek()
    none_type_9 = None
    queue_node_13 = module_0.QueueNode(none_type_9)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_12 = queue_10.__len__()
    assert var_12 == 0
    none_type_10 = None
    queue_node_14 = module_0.QueueNode(none_type_10)
    tuple_2 = ()
    queue_node_15 = module_0.QueueNode(tuple_2)
    var_13 = queue_10.clear()
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0

def test_case_56():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_2 = queue_5.__len__()
    assert var_2 == 0
    var_3 = queue_5.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    var_5 = queue_4.peek()
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    tuple_0 = ()
    queue_node_7 = module_0.QueueNode(tuple_0)
    var_7 = queue_6.clear()
    queue_node_8 = module_0.QueueNode(queue_1)
    assert len(queue_node_8.data) == 0

def test_case_57():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0

def test_case_58():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    tuple_1 = ()
    queue_node_3 = module_0.QueueNode(tuple_1)
    str_0 = 'a,~'
    queue_node_4 = module_0.QueueNode(str_0)
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    var_2 = queue_2.enqueue(none_type_2)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    queue_node_8 = module_0.QueueNode(none_type_4)
    var_4 = queue_4.__str__()

def test_case_59():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_4.peek()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_6 = module_0.QueueNode(tuple_0)
    var_9 = queue_6.clear()
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    tuple_1 = ()
    queue_node_8 = module_0.QueueNode(tuple_1)
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_10 = queue_7.__len__()
    assert var_10 == 0
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_11 = queue_8.__len__()
    assert var_11 == 0
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_8 = None
    queue_node_11 = module_0.QueueNode(none_type_8)
    var_12 = queue_9.enqueue(none_type_7)
    assert len(queue_9) == 1
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0
    var_13 = queue_8.peek()

def test_case_60():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_4 = queue_3.enqueue(none_type_1)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_6 = module_0.QueueNode(tuple_0)
    var_6 = queue_5.clear()
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    var_8 = queue_8.enqueue(none_type_5)
    assert len(queue_8) == 1
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    none_type_8 = None
    queue_node_10 = module_0.QueueNode(none_type_8)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_9 = queue_9.__len__()
    assert var_9 == 0
    var_10 = queue_8.enqueue(queue_node_6)
    assert len(queue_8) == 2

def test_case_61():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_0 = queue_3.__len__()
    assert var_0 == 0
    var_1 = queue_3.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_2.peek()
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    str_0 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_0)
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    var_8 = queue_6.clear()
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    queue_node_8 = module_0.QueueNode(none_type_5)
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_10 = module_0.QueueNode(tuple_1)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_10 = queue_8.__str__()
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    tuple_2 = ()
    queue_node_12 = module_0.QueueNode(tuple_2)
    var_11 = queue_0.__len__()
    assert var_11 == 0

def test_case_62():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    var_2 = queue_2.enqueue(none_type_3)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_3 = queue_6.__len__()
    assert var_3 == 0
    var_4 = queue_6.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    var_6 = queue_5.peek()
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    queue_node_9 = module_0.QueueNode(none_type_6)
    str_0 = 'a,~'
    queue_node_10 = module_0.QueueNode(str_0)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0

def test_case_63():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    str_0 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_0)
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__str__()
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0

def test_case_64():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_1 = queue_1.enqueue(none_type_1)
    assert len(queue_1) == 1
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_3 = queue_5.__len__()
    assert var_3 == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    none_type_5 = None
    queue_node_5 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_6 = None
    queue_node_6 = module_0.QueueNode(none_type_6)
    var_7 = queue_7.enqueue(none_type_5)
    assert len(queue_7) == 1
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_7 = None
    queue_node_7 = module_0.QueueNode(none_type_7)
    tuple_0 = ()
    queue_node_8 = module_0.QueueNode(tuple_0)
    none_type_8 = None
    queue_node_9 = module_0.QueueNode(none_type_8)
    tuple_1 = ()
    queue_node_10 = module_0.QueueNode(tuple_1)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_8 = queue_9.__str__()
    var_9 = queue_7.peek()

def test_case_65():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_node_3 = module_0.QueueNode(none_type_1)
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    var_3 = queue_3.enqueue(none_type_2)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0

def test_case_66():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    str_0 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_4.peek()
    var_8 = queue_4.clear()

def test_case_67():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_6 = module_0.QueueNode(tuple_0)
    var_4 = queue_3.clear()
    str_0 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_10 = module_0.QueueNode(tuple_1)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__str__()
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    tuple_2 = ()
    queue_node_12 = module_0.QueueNode(tuple_2)
    var_9 = queue_5.peek()

def test_case_68():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_2 = queue_4.__len__()
    assert var_2 == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    var_6 = queue_5.clear()
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_7 = queue_8.__len__()
    assert var_7 == 0
    var_8 = queue_8.__len__()
    assert var_8 == 0
    var_9 = var_8.__str__()
    assert var_9 == '0'
    var_10 = queue_7.peek()
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_6 = None
    queue_node_7 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_8 = module_0.QueueNode(tuple_1)
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0

def test_case_69():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_6 = module_0.QueueNode(tuple_1)
    str_0 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_0)
    var_5 = queue_4.__len__()
    assert var_5 == 0

def test_case_70():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_4 = queue_3.enqueue(none_type_1)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_5 = queue_7.__len__()
    assert var_5 == 0
    var_6 = queue_7.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    var_8 = queue_6.peek()
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    none_type_6 = None
    queue_node_7 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_8 = module_0.QueueNode(tuple_1)
    var_10 = queue_8.clear()
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    str_0 = 'a,~'
    queue_node_10 = module_0.QueueNode(str_0)
    none_type_8 = None
    queue_node_11 = module_0.QueueNode(none_type_8)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_11 = queue_9.__len__()
    assert var_11 == 0
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    none_type_9 = None
    queue_node_12 = module_0.QueueNode(none_type_9)
    var_12 = queue_10.enqueue(none_type_8)
    assert len(queue_10) == 1
    none_type_10 = None
    queue_node_13 = module_0.QueueNode(none_type_10)
    tuple_2 = ()
    queue_node_14 = module_0.QueueNode(tuple_2)
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0
    var_13 = queue_11.__str__()
    queue_12 = module_0.Queue()
    assert len(queue_12) == 0
    var_14 = var_1.__str__()
    assert var_14 == '0'

def test_case_71():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_2 = queue_4.__len__()
    assert var_2 == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    var_5 = queue_3.peek()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    queue_node_5 = module_0.QueueNode(none_type_3)
    var_7 = queue_3.__str__()

def test_case_72():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    queue_node_3 = module_0.QueueNode(none_type_1)

def test_case_73():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_0.clear()

def test_case_74():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    queue_node_3 = module_0.QueueNode(queue_1)
    assert len(queue_node_3.data) == 0

def test_case_75():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    var_2 = var_1.__str__()

def test_case_76():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0

def test_case_77():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_node_5 = module_0.QueueNode(tuple_0)

def test_case_78():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    var_2 = queue_1.clear()
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0

def test_case_79():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_1.clear()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    var_4 = queue_4.enqueue(none_type_3)
    assert len(queue_4) == 1
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_5 = queue_8.__len__()
    assert var_5 == 0
    var_6 = queue_8.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    var_8 = queue_7.peek()
    none_type_6 = None
    queue_node_7 = module_0.QueueNode(none_type_6)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_9 = queue_9.__len__()
    assert var_9 == 0
    queue_node_8 = module_0.QueueNode(none_type_6)
    str_0 = 'a,~'
    queue_node_9 = module_0.QueueNode(str_0)
    var_10 = queue_0.peek()

def test_case_80():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0

def test_case_81():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__str__()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    var_3 = queue_3.clear()
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_4 = queue_6.__len__()
    assert var_4 == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_5.peek()
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_8 = queue_8.__len__()
    assert var_8 == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    var_10 = var_9.__str__()
    assert var_10 == '0'
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    tuple_2 = ()
    queue_node_9 = module_0.QueueNode(tuple_2)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_11 = queue_9.__len__()
    assert var_11 == 0
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_12 = queue_10.__len__()
    assert var_12 == 0
    queue_node_11 = module_0.QueueNode(none_type_7)
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0

def test_case_82():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    queue_node_8 = module_0.QueueNode(none_type_5)
    str_0 = 'a,~'
    queue_node_9 = module_0.QueueNode(str_0)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_6 = None
    queue_node_10 = module_0.QueueNode(none_type_6)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_6 = queue_8.__len__()
    assert var_6 == 0
    var_7 = queue_8.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    var_9 = queue_7.peek()
    var_10 = queue_1.peek()

def test_case_83():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_2 = queue_2.enqueue(none_type_0)
    assert len(queue_2) == 1
    queue_node_2 = module_0.QueueNode(var_1)
    assert queue_node_2.data == 0

def test_case_84():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)

def test_case_85():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__str__()
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    tuple_1 = ()
    queue_node_7 = module_0.QueueNode(tuple_1)
    queue_node_8 = module_0.QueueNode(queue_2)
    assert len(queue_node_8.data) == 0

def test_case_86():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0

def test_case_87():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    str_0 = 'a,~'
    queue_node_5 = module_0.QueueNode(str_0)
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    tuple_1 = ()
    queue_node_8 = module_0.QueueNode(tuple_1)
    var_8 = queue_7.clear()
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_9 = queue_9.__len__()
    assert var_9 == 0
    var_10 = queue_9.__len__()
    assert var_10 == 0
    var_11 = var_10.__str__()
    assert var_11 == '0'
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    tuple_2 = ()
    queue_node_11 = module_0.QueueNode(tuple_2)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_12 = queue_10.__str__()
    var_13 = queue_3.enqueue(var_8)
    assert len(queue_3) == 1

def test_case_88():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_node_2 = module_0.QueueNode(none_type_1)
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_1.peek()

def test_case_89():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_node_3 = module_0.QueueNode(none_type_1)
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    var_3 = queue_3.enqueue(none_type_2)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    str_0 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_0)
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_10 = module_0.QueueNode(tuple_1)
    var_8 = queue_7.clear()
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    tuple_2 = ()
    queue_node_12 = module_0.QueueNode(tuple_2)
    none_type_8 = None
    queue_node_13 = module_0.QueueNode(none_type_8)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    var_10 = var_9.__str__()
    assert var_10 == '0'

def test_case_90():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    var_5 = queue_2.clear()

def test_case_91():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__str__()
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0

def test_case_92():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_6 = module_0.QueueNode(tuple_0)
    var_6 = queue_4.clear()
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_7 = queue_5.__len__()
    assert var_7 == 0
    queue_node_7 = module_0.QueueNode(var_4)
    assert queue_node_7.data == 0

def test_case_93():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    var_5 = queue_2.peek()
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    var_7 = queue_5.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0

def test_case_94():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    str_1 = 'a,~'
    queue_node_4 = module_0.QueueNode(str_1)
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_6 = queue_7.__len__()
    assert var_6 == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_8 = module_0.QueueNode(tuple_0)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_9 = queue_9.__str__()
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0

def test_case_95():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0

def test_case_96():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    var_4 = queue_0.__str__()

def test_case_97():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_4 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    var_4 = queue_5.enqueue(none_type_3)
    assert len(queue_5) == 1
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_10 = module_0.QueueNode(tuple_1)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_6 = queue_8.__len__()
    assert var_6 == 0
    var_7 = queue_8.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0

def test_case_98():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_1 = queue_3.__len__()
    assert var_1 == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    var_4 = queue_2.peek()
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    var_9 = queue_4.enqueue(queue_0)
    assert len(queue_4) == 1

def test_case_99():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    str_0 = 'a,~'
    queue_node_8 = module_0.QueueNode(str_0)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_7 = queue_8.__len__()
    assert var_7 == 0
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    tuple_2 = ()
    queue_node_11 = module_0.QueueNode(tuple_2)
    var_8 = queue_8.clear()
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_9 = queue_9.__len__()
    assert var_9 == 0
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0
    none_type_8 = None
    queue_node_12 = module_0.QueueNode(none_type_8)
    queue_12 = module_0.Queue()
    assert len(queue_12) == 0
    var_10 = queue_12.__len__()
    assert var_10 == 0
    var_11 = queue_12.__len__()
    assert var_11 == 0
    var_12 = var_11.__str__()
    assert var_12 == '0'
    var_13 = queue_11.peek()
    var_14 = var_6.__str__()
    assert var_14 == '0'

def test_case_100():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__str__()
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    queue_node_4 = module_0.QueueNode(queue_node_3)
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_6 = module_0.QueueNode(tuple_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    none_type_3 = None
    queue_node_7 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_4 = None
    queue_node_8 = module_0.QueueNode(none_type_4)
    var_6 = queue_6.enqueue(none_type_3)
    assert len(queue_6) == 1
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    str_1 = 'a,~'
    queue_node_9 = module_0.QueueNode(str_1)
    var_7 = var_2.__len__()

def test_case_101():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1

def test_case_102():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    str_0 = 'JLcd4+\n\\'
    var_9 = queue_1.enqueue(str_0)
    assert len(queue_1) == 1

def test_case_103():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    none_type_0 = None
    queue_node_1 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.enqueue(queue_1)
    assert len(queue_1) == 1
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    var_3 = queue_3.enqueue(none_type_1)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    str_1 = 'a,~'
    queue_node_5 = module_0.QueueNode(str_1)
    queue_node_6 = module_0.QueueNode(queue_node_5)
    queue_node_7 = module_0.QueueNode(queue_node_6)

def test_case_104():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0

def test_case_105():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    queue_node_4 = module_0.QueueNode(queue_node_3)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    var_5 = queue_2.peek()
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    var_7 = queue_5.enqueue(none_type_3)
    assert len(queue_5) == 1
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__len__()
    assert var_8 == 0
    queue_node_9 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    var_10 = queue_6.enqueue(tuple_0)
    assert len(queue_6) == 1

def test_case_106():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    var_2 = queue_1.clear()
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'

def test_case_107():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__str__()
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    var_8 = queue_7.enqueue(none_type_3)
    assert len(queue_7) == 1
    str_0 = 'a,~'
    queue_node_6 = module_0.QueueNode(str_0)
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    queue_node_8 = module_0.QueueNode(none_type_5)
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_10 = queue_9.__len__()
    assert var_10 == 0
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_11 = queue_10.__len__()
    assert var_11 == 0
    str_1 = 'a,~'
    queue_node_10 = module_0.QueueNode(str_1)
    queue_node_11 = module_0.QueueNode(queue_node_10)
    none_type_7 = None
    queue_node_12 = module_0.QueueNode(none_type_7)
    tuple_1 = ()
    queue_node_13 = module_0.QueueNode(tuple_1)
    queue_node_14 = module_0.QueueNode(queue_node_6)

def test_case_108():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    none_type_0 = None
    queue_node_1 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_2 = queue_4.__len__()
    assert var_2 == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.enqueue(queue_6)
    assert len(queue_6) == 1
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_6 = queue_7.__len__()
    assert var_6 == 0
    queue_node_8 = module_0.QueueNode(none_type_4)
    var_7 = queue_4.peek()

def test_case_109():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    queue_node_2 = module_0.QueueNode(queue_node_1)
    str_1 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_1)
    var_2 = queue_0.clear()

def test_case_110():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_2 = queue_1.__str__()
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    str_0 = 'a,~'
    queue_node_6 = module_0.QueueNode(str_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_7 = queue_5.__len__()
    assert var_7 == 0
    queue_node_9 = module_0.QueueNode(none_type_5)
    none_type_6 = None
    queue_node_10 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    var_10 = queue_8.__len__()
    assert var_10 == 0
    var_11 = var_10.__str__()
    assert var_11 == '0'
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_12 = queue_10.enqueue(queue_10)
    assert len(queue_10) == 1
    var_13 = queue_8.__len__()
    assert var_13 == 0

def test_case_111():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()

def test_case_112():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    var_3 = queue_2.clear()
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0

def test_case_113():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    str_0 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_0)
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    queue_node_6 = module_0.QueueNode(none_type_3)
    str_1 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_1)
    queue_node_8 = module_0.QueueNode(queue_node_7)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.enqueue(queue_6)
    assert len(queue_6) == 1
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0

def test_case_114():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__str__()
    var_2 = queue_1.clear()

def test_case_115():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_1 = queue_3.__len__()
    assert var_1 == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    var_4 = queue_2.peek()
    str_0 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_0)
    queue_node_3 = module_0.QueueNode(queue_node_2)
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_6 = module_0.QueueNode(tuple_0)
    var_6 = queue_4.clear()
    var_7 = queue_1.peek()

def test_case_116():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_2 = queue_0.__str__()
    queue_node_2 = module_0.QueueNode(var_2)

def test_case_117():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.enqueue(queue_1)
    assert len(queue_1) == 1
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__str__()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_3 = queue_5.__len__()
    assert var_3 == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    str_0 = 'a,~'
    queue_node_6 = module_0.QueueNode(str_0)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_6 = queue_7.__len__()
    assert var_6 == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    queue_node_8 = module_0.QueueNode(var_7)
    assert queue_node_8.data == 0

def test_case_118():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_2 = queue_0.__str__()
    queue_node_2 = module_0.QueueNode(var_2)
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_3 = queue_1.__len__()
    assert var_3 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_3.peek()
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    var_10 = queue_8.enqueue(none_type_4)
    assert len(queue_8) == 1
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_10 = module_0.QueueNode(tuple_1)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_11 = queue_9.__str__()
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_12 = queue_10.enqueue(queue_10)
    assert len(queue_10) == 1
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    var_13 = queue_10.peek()
    assert len(var_13) == 1

def test_case_119():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    str_1 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_3 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    none_type_1 = None
    queue_node_4 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_6 = module_0.QueueNode(tuple_0)
    var_4 = queue_2.clear()
    none_type_3 = None
    queue_node_7 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_5 = queue_3.__len__()
    assert var_5 == 0
    var_6 = queue_3.peek()
    str_2 = 'a,~'
    queue_node_8 = module_0.QueueNode(str_2)
    var_7 = queue_3.__str__()
    queue_node_9 = module_0.QueueNode(var_7)
    none_type_4 = None
    queue_node_10 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_8 = queue_4.__len__()
    assert var_8 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_11 = module_0.QueueNode(none_type_5)
    var_9 = queue_5.enqueue(none_type_4)
    assert len(queue_5) == 1
    none_type_6 = None
    queue_node_12 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_10 = queue_6.__len__()
    assert var_10 == 0
    queue_node_13 = module_0.QueueNode(none_type_6)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0

def test_case_120():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.enqueue(queue_2)
    assert len(queue_2) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__str__()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    queue_node_5 = module_0.QueueNode(none_type_3)
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_7 = module_0.QueueNode(tuple_1)
    var_5 = var_2.__str__()

def test_case_121():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.peek()
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_2 = queue_1.__str__()
    queue_node_2 = module_0.QueueNode(var_2)
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    var_4 = queue_3.enqueue(none_type_1)
    assert len(queue_3) == 1
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    var_6 = queue_4.peek()
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_7 = queue_5.__len__()
    assert var_7 == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__len__()
    assert var_8 == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    var_10 = var_9.__str__()
    assert var_10 == '0'
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_11 = queue_8.enqueue(queue_8)
    assert len(queue_8) == 1
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_12 = queue_9.__len__()
    assert var_12 == 0
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_13 = queue_10.__len__()
    assert var_13 == 0
    var_14 = var_13.__str__()
    assert var_14 == '0'

def test_case_122():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_3 = queue_5.__len__()
    assert var_3 == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    tuple_0 = ()
    queue_node_7 = module_0.QueueNode(tuple_0)
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_9 = module_0.QueueNode(tuple_1)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_6 = queue_7.__str__()
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_7 = queue_8.enqueue(queue_8)
    assert len(queue_8) == 1
    str_0 = 'a,~'
    queue_node_10 = module_0.QueueNode(str_0)
    queue_node_11 = module_0.QueueNode(queue_node_10)
    queue_node_12 = module_0.QueueNode(var_7)

def test_case_123():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    var_2 = queue_3.enqueue(none_type_2)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_3 = queue_6.__len__()
    assert var_3 == 0
    var_4 = queue_6.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_6 = queue_8.__len__()
    assert var_6 == 0
    queue_node_8 = module_0.QueueNode(none_type_5)
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_7 = queue_9.__len__()
    assert var_7 == 0
    var_8 = queue_9.peek()
    var_9 = queue_7.__str__()

def test_case_124():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_1 = queue_3.__len__()
    assert var_1 == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    var_4 = queue_2.peek()
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = queue_5.peek()
    str_0 = 'a,~'
    queue_node_4 = module_0.QueueNode(str_0)
    var_7 = queue_5.__str__()
    queue_node_5 = module_0.QueueNode(var_7)
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    queue_node_7 = module_0.QueueNode(none_type_3)
    str_1 = 'a,~'
    queue_node_8 = module_0.QueueNode(str_1)
    queue_node_9 = module_0.QueueNode(queue_node_8)
    none_type_4 = None
    queue_node_10 = module_0.QueueNode(none_type_4)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_5 = None
    queue_node_11 = module_0.QueueNode(none_type_5)
    var_10 = queue_8.enqueue(none_type_4)
    assert len(queue_8) == 1
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_6 = None
    queue_node_12 = module_0.QueueNode(none_type_6)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_11 = queue_10.__len__()
    assert var_11 == 0
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0
    none_type_7 = None
    queue_node_13 = module_0.QueueNode(none_type_7)
    var_12 = queue_11.enqueue(none_type_6)
    assert len(queue_11) == 1
    queue_12 = module_0.Queue()
    assert len(queue_12) == 0

def test_case_125():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    var_3 = queue_2.clear()
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    queue_node_7 = module_0.QueueNode(none_type_5)
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    var_7 = queue_5.peek()
    none_type_8 = None
    queue_node_10 = module_0.QueueNode(none_type_8)
    tuple_1 = ()
    queue_node_11 = module_0.QueueNode(tuple_1)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__str__()
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_9 = None
    queue_node_12 = module_0.QueueNode(none_type_9)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    var_10 = queue_8.__len__()
    assert var_10 == 0
    var_11 = var_10.__str__()
    assert var_11 == '0'
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0

def test_case_126():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__str__()
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.enqueue(queue_6)
    assert len(queue_6) == 1
    str_0 = 'a,~'
    queue_node_6 = module_0.QueueNode(str_0)
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    var_8 = queue_7.peek()
    str_1 = 'a,~'
    queue_node_8 = module_0.QueueNode(str_1)
    var_9 = queue_7.__str__()
    queue_node_9 = module_0.QueueNode(var_9)
    none_type_5 = None
    queue_node_10 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_10 = queue_8.__len__()
    assert var_10 == 0
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_6 = None
    queue_node_11 = module_0.QueueNode(none_type_6)
    var_11 = queue_9.enqueue(none_type_5)
    assert len(queue_9) == 1
    var_12 = queue_5.enqueue(queue_node_11)
    assert len(queue_5) == 1

def test_case_127():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    str_0 = 'a,~'
    queue_node_6 = module_0.QueueNode(str_0)
    str_1 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_1)
    queue_node_8 = module_0.QueueNode(queue_node_7)
    none_type_4 = None
    queue_node_9 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    none_type_5 = None
    queue_node_10 = module_0.QueueNode(none_type_5)
    tuple_1 = ()
    queue_node_11 = module_0.QueueNode(tuple_1)
    var_5 = queue_5.clear()
    none_type_6 = None
    queue_node_12 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_7 = None
    queue_node_13 = module_0.QueueNode(none_type_7)
    var_7 = queue_7.enqueue(none_type_6)
    assert len(queue_7) == 1
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_8 = queue_6.peek()

def test_case_128():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_2 = queue_1.__len__()
    assert var_2 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_3 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = queue_4.peek()
    str_0 = 'a,~'
    queue_node_4 = module_0.QueueNode(str_0)
    var_6 = queue_4.__str__()
    queue_node_5 = module_0.QueueNode(var_6)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0

def test_case_129():
    dict_0 = {}
    queue_node_0 = module_0.QueueNode(dict_0)

def test_case_130():
    dict_0 = {}
    queue_node_0 = module_0.QueueNode(dict_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_0 = None
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = queue_1.peek()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    var_4 = queue_2.clear()
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_5 = queue_3.__len__()
    assert var_5 == 0
    queue_node_7 = module_0.QueueNode(none_type_4)
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_7 = queue_5.__len__()
    assert var_7 == 0
    var_8 = queue_5.peek()
    str_0 = 'a,~'
    queue_node_10 = module_0.QueueNode(str_0)
    var_9 = queue_5.__str__()
    queue_node_11 = module_0.QueueNode(var_9)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_10 = queue_6.enqueue(queue_6)
    assert len(queue_6) == 1
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    queue_node_12 = module_0.QueueNode(queue_2)
    assert len(queue_node_12.data) == 0

def test_case_131():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_2 = queue_0.__str__()
    queue_node_2 = module_0.QueueNode(var_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    var_6 = queue_2.peek()
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_7 = queue_4.enqueue(queue_4)
    assert len(queue_4) == 1
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    var_9 = queue_6.__len__()
    assert var_9 == 0
    var_10 = var_9.__str__()
    assert var_10 == '0'
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    dict_0 = {}
    queue_node_5 = module_0.QueueNode(dict_0)
    var_11 = queue_5.peek()

def test_case_132():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)

def test_case_133():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    bool_0 = True
    var_0 = queue_0.enqueue(bool_0)
    assert len(queue_0) == 1

def test_case_134():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_2 = queue_0.__str__()
    queue_node_2 = module_0.QueueNode(var_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    var_4 = queue_2.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    var_7 = queue_5.enqueue(none_type_3)
    assert len(queue_5) == 1
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    tuple_0 = ()
    queue_node_8 = module_0.QueueNode(tuple_0)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_8 = queue_8.__len__()
    assert var_8 == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    var_10 = var_9.__str__()
    assert var_10 == '0'
    str_1 = 'a,~'
    queue_node_10 = module_0.QueueNode(str_1)
    queue_node_11 = module_0.QueueNode(queue_node_10)
    none_type_7 = None
    queue_node_12 = module_0.QueueNode(none_type_7)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_11 = queue_9.__len__()
    assert var_11 == 0
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    none_type_8 = None
    queue_node_13 = module_0.QueueNode(none_type_8)
    var_12 = queue_10.enqueue(none_type_7)
    assert len(queue_10) == 1
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0
    queue_node_14 = module_0.QueueNode(queue_1)
    assert len(queue_node_14.data) == 0

def test_case_135():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    str_0 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_0)
    queue_node_3 = module_0.QueueNode(queue_node_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_2 = queue_4.__len__()
    assert var_2 == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    var_6 = queue_6.enqueue(none_type_3)
    assert len(queue_6) == 1
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_node_8 = module_0.QueueNode(queue_node_7)
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    tuple_0 = ()
    queue_node_10 = module_0.QueueNode(tuple_0)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_7 = queue_7.__str__()
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_8 = var_4.__len__()

def test_case_136():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    none_type_0 = None
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_0.peek()

def test_case_137():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    bool_0 = True
    var_0 = queue_0.enqueue(bool_0)
    assert len(queue_0) == 1
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = queue_1.peek()
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    var_3 = queue_1.__str__()
    queue_node_4 = module_0.QueueNode(var_3)
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    queue_node_6 = module_0.QueueNode(queue_node_5)
    none_type_3 = None
    queue_node_7 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_4 = queue_2.__len__()
    assert var_4 == 0
    var_5 = var_1.__str__()
    assert var_5 == '0'

def test_case_138():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    str_0 = 'a,~'
    queue_node_4 = module_0.QueueNode(str_0)
    var_2 = queue_0.__str__()
    queue_node_5 = module_0.QueueNode(var_2)
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_3 = queue_1.__len__()
    assert var_3 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    var_4 = queue_2.enqueue(none_type_3)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    tuple_0 = ()
    queue_node_10 = module_0.QueueNode(tuple_0)
    var_6 = queue_4.clear()
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    var_9 = var_8.__str__()
    assert var_9 == '0'
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    str_1 = 'a,~'
    queue_node_12 = module_0.QueueNode(str_1)
    var_10 = queue_2.enqueue(queue_node_4)
    assert len(queue_2) == 2

def test_case_139():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_2 = queue_0.__str__()
    queue_node_2 = module_0.QueueNode(var_2)
    var_3 = queue_0.enqueue(var_0)
    assert len(queue_0) == 1

def test_case_140():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.peek()
    str_0 = 'a,~'
    queue_node_5 = module_0.QueueNode(str_0)
    var_3 = queue_2.__str__()
    queue_node_6 = module_0.QueueNode(var_3)
    str_1 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_1)
    queue_node_8 = module_0.QueueNode(queue_node_7)
    none_type_3 = None
    queue_node_9 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_10 = module_0.QueueNode(tuple_1)
    none_type_4 = None
    queue_node_11 = module_0.QueueNode(none_type_4)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    var_5 = queue_3.peek()
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_5 = None
    queue_node_12 = module_0.QueueNode(none_type_5)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    var_7 = queue_5.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    none_type_6 = None
    queue_node_13 = module_0.QueueNode(none_type_6)
    var_10 = var_8.__len__()

def test_case_141():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_2 = queue_2.enqueue(none_type_0)
    assert len(queue_2) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_6 = queue_7.__len__()
    assert var_6 == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    tuple_0 = ()
    queue_node_7 = module_0.QueueNode(tuple_0)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_9 = queue_10.__len__()
    assert var_9 == 0
    var_10 = queue_10.__len__()
    assert var_10 == 0
    var_11 = var_10.__str__()
    assert var_11 == '0'
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0
    var_12 = queue_11.__len__()
    assert var_12 == 0
    none_type_8 = None
    queue_node_10 = module_0.QueueNode(none_type_8)
    tuple_1 = ()
    queue_node_11 = module_0.QueueNode(tuple_1)
    var_13 = queue_11.clear()
    queue_node_12 = module_0.QueueNode(var_11)
    assert queue_node_12.data == '0'

def test_case_142():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    dict_0 = {}
    queue_node_1 = module_0.QueueNode(dict_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_7 = queue_5.__len__()
    assert var_7 == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    var_8 = queue_6.enqueue(none_type_2)
    assert len(queue_6) == 1
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    tuple_0 = ()
    queue_node_8 = module_0.QueueNode(tuple_0)
    var_10 = queue_8.clear()
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_11 = queue_9.__len__()
    assert var_11 == 0
    var_12 = queue_9.peek()
    var_13 = queue_2.__str__()

def test_case_143():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = queue_1.peek()
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_7 = module_0.QueueNode(tuple_1)
    var_4 = queue_2.clear()
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_5 = queue_3.__len__()
    assert var_5 == 0
    dict_0 = {}
    queue_node_8 = module_0.QueueNode(dict_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_5 = None
    queue_node_9 = module_0.QueueNode(none_type_5)
    queue_node_10 = module_0.QueueNode(queue_node_9)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_6 = None
    queue_node_11 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    queue_node_12 = module_0.QueueNode(none_type_3)

def test_case_144():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_2 = queue_0.__str__()
    queue_node_2 = module_0.QueueNode(var_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_3 = queue_1.__len__()
    assert var_3 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    var_5 = queue_3.clear()
    dict_0 = {}
    queue_node_6 = module_0.QueueNode(dict_0)
    none_type_3 = None
    queue_node_7 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_8 = module_0.QueueNode(none_type_4)
    var_7 = queue_5.enqueue(none_type_3)
    assert len(queue_5) == 1
    str_1 = 'a,~'
    queue_node_9 = module_0.QueueNode(str_1)
    none_type_5 = None
    queue_node_10 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    queue_node_11 = module_0.QueueNode(none_type_5)
    none_type_6 = None
    queue_node_12 = module_0.QueueNode(none_type_6)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    queue_node_13 = module_0.QueueNode(var_7)

def test_case_145():
    int_0 = 417
    tuple_0 = (int_0, int_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(tuple_0)
    assert len(queue_0) == 1

def test_case_146():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_4 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    dict_0 = {}
    queue_node_6 = module_0.QueueNode(dict_0)
    none_type_3 = None
    queue_node_7 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = queue_4.peek()
    str_1 = 'a,~'
    queue_node_8 = module_0.QueueNode(str_1)
    var_5 = queue_4.__str__()
    queue_node_9 = module_0.QueueNode(var_5)
    none_type_4 = None
    queue_node_10 = module_0.QueueNode(none_type_4)
    queue_node_11 = module_0.QueueNode(queue_node_10)
    var_6 = queue_4.__str__()

def test_case_147():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    var_4 = queue_3.enqueue(none_type_2)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    str_1 = 'a,~'
    queue_node_6 = module_0.QueueNode(str_1)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_8 = module_0.QueueNode(tuple_0)
    bool_0 = True
    var_5 = queue_6.enqueue(bool_0)
    assert len(queue_6) == 1
    none_type_5 = None
    queue_node_9 = module_0.QueueNode(none_type_5)
    queue_node_10 = module_0.QueueNode(queue_node_9)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_6 = None
    queue_node_11 = module_0.QueueNode(none_type_6)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_6 = queue_9.__len__()
    assert var_6 == 0
    var_7 = queue_9.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    var_9 = queue_8.peek()
    none_type_7 = None
    queue_node_12 = module_0.QueueNode(none_type_7)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_10 = queue_10.__len__()
    assert var_10 == 0
    var_11 = queue_10.peek()
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0

def test_case_148():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    dict_0 = {}
    queue_node_2 = module_0.QueueNode(dict_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_3 = queue_6.__len__()
    assert var_3 == 0
    var_4 = queue_6.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    var_6 = queue_5.peek()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    queue_node_5 = module_0.QueueNode(none_type_3)
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_8 = queue_8.__len__()
    assert var_8 == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_9 = queue_9.__len__()
    assert var_9 == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    tuple_0 = ()
    queue_node_9 = module_0.QueueNode(tuple_0)
    var_10 = queue_9.clear()
    var_11 = var_1.__str__()
    assert var_11 == '0'

def test_case_149():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    var_2 = var_0.__str__()
    assert var_2 == '0'

def test_case_150():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    var_2 = queue_1.clear()
    int_0 = 417
    tuple_1 = (int_0, int_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.enqueue(tuple_1)
    assert len(queue_2) == 1
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    tuple_2 = ()
    queue_node_7 = module_0.QueueNode(tuple_2)
    bool_0 = True
    var_7 = queue_5.enqueue(bool_0)
    assert len(queue_5) == 1
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    var_9 = queue_6.peek()
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_10 = queue_9.__len__()
    assert var_10 == 0
    var_11 = queue_9.__len__()
    assert var_11 == 0
    var_12 = var_11.__str__()
    assert var_12 == '0'
    var_13 = queue_8.peek()
    var_14 = queue_1.clear()

def test_case_151():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_2 = queue_1.enqueue(queue_1)
    assert len(queue_1) == 1
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_3 = var_2.__str__()

def test_case_152():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    bool_0 = True
    var_1 = queue_1.enqueue(bool_0)
    assert len(queue_1) == 1
    dict_0 = {}
    queue_node_2 = module_0.QueueNode(dict_0)
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    str_0 = 'a,~'
    queue_node_6 = module_0.QueueNode(str_0)
    none_type_3 = None
    queue_node_7 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_4 = None
    queue_node_8 = module_0.QueueNode(none_type_4)
    var_7 = queue_7.enqueue(none_type_3)
    assert len(queue_7) == 1
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0

def test_case_153():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    dict_0 = {}
    queue_node_0 = module_0.QueueNode(dict_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.enqueue(queue_1)
    assert len(queue_1) == 1
    none_type_0 = None
    queue_node_1 = module_0.QueueNode(none_type_0)
    int_0 = 417
    tuple_0 = (int_0, int_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.enqueue(tuple_0)
    assert len(queue_2) == 1
    str_0 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_0)
    queue_node_3 = module_0.QueueNode(queue_node_2)
    none_type_1 = None
    queue_node_4 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    var_4 = queue_4.enqueue(none_type_1)
    assert len(queue_4) == 1
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_5 = queue_7.__len__()
    assert var_5 == 0
    var_6 = queue_7.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    var_8 = queue_6.peek()
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_8 = module_0.QueueNode(tuple_1)
    str_1 = 'a,~'
    queue_node_9 = module_0.QueueNode(str_1)
    bytes_0 = b'\x9bn\xaa\xf4\x02\xd9\xbc\x9ax\xa40\x8d\xca\xd0\xfd\xc7'
    queue_node_10 = module_0.QueueNode(bytes_0)

def test_case_154():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.peek()
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    queue_node_2 = module_0.QueueNode(queue_node_1)
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = queue_2.peek()
    str_1 = 'a,~'
    queue_node_6 = module_0.QueueNode(str_1)
    var_4 = queue_2.__str__()
    queue_node_7 = module_0.QueueNode(var_4)
    none_type_3 = None
    queue_node_8 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_5 = queue_3.__len__()
    assert var_5 == 0
    queue_node_9 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_10 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    var_9 = queue_5.peek()
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_5 = None
    queue_node_11 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_10 = queue_8.__len__()
    assert var_10 == 0
    var_11 = queue_8.__len__()
    assert var_11 == 0
    var_12 = var_11.__str__()
    assert var_12 == '0'
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_6 = None
    queue_node_12 = module_0.QueueNode(none_type_6)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_13 = queue_10.__len__()
    assert var_13 == 0
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0
    none_type_7 = None
    queue_node_13 = module_0.QueueNode(none_type_7)
    var_14 = queue_11.enqueue(none_type_6)
    assert len(queue_11) == 1
    var_15 = queue_0.peek()

def test_case_155():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_3 = queue_5.__len__()
    assert var_3 == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_node_6 = module_0.QueueNode(queue_node_5)
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_6 = queue_7.__len__()
    assert var_6 == 0
    var_7 = queue_7.peek()
    str_0 = 'a,~'
    queue_node_8 = module_0.QueueNode(str_0)
    var_8 = queue_7.__str__()
    queue_node_9 = module_0.QueueNode(var_8)
    str_1 = 'a,~'
    queue_node_10 = module_0.QueueNode(str_1)
    none_type_6 = None
    queue_node_11 = module_0.QueueNode(none_type_6)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    none_type_7 = None
    queue_node_12 = module_0.QueueNode(none_type_7)
    tuple_1 = ()
    queue_node_13 = module_0.QueueNode(tuple_1)
    var_10 = queue_8.clear()
    int_0 = 417
    tuple_2 = (int_0, int_0)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_11 = queue_9.enqueue(tuple_2)
    assert len(queue_9) == 1
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    none_type_8 = None
    queue_node_14 = module_0.QueueNode(none_type_8)
    tuple_3 = ()
    queue_node_15 = module_0.QueueNode(tuple_3)
    bool_0 = True
    var_12 = queue_10.enqueue(bool_0)
    assert len(queue_10) == 1
    none_type_9 = None
    queue_node_16 = module_0.QueueNode(none_type_9)
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0

def test_case_156():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    var_2 = queue_1.clear()

def test_case_157():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_node_4 = module_0.QueueNode(none_type_2)
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_1.enqueue(none_type_4)
    assert len(queue_1) == 1

def test_case_158():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.peek()

def test_case_159():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    queue_node_4 = module_0.QueueNode(none_type_2)
    var_5 = queue_4.clear()
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_node_6 = module_0.QueueNode(queue_node_5)
    var_6 = var_0.__str__()
    assert var_6 == '0'

def test_case_160():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.enqueue(queue_1)
    assert len(queue_1) == 1
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_2 = queue_3.enqueue(none_type_1)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_3 = queue_5.__len__()
    assert var_3 == 0
    str_0 = 'a,~'
    queue_node_4 = module_0.QueueNode(str_0)
    queue_node_5 = module_0.QueueNode(queue_node_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_4 = queue_8.__len__()
    assert var_4 == 0
    var_5 = queue_8.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_7.peek()
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_8 = queue_9.__len__()
    assert var_8 == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    tuple_1 = ()
    queue_node_9 = module_0.QueueNode(tuple_1)
    var_9 = queue_9.clear()
    var_10 = queue_6.clear()

def test_case_161():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    dict_0 = {}
    queue_node_0 = module_0.QueueNode(dict_0)
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_1 = queue_0.enqueue(str_0)
    assert len(queue_0) == 1

def test_case_162():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_2 = queue_2.enqueue(none_type_0)
    assert len(queue_2) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0

def test_case_163():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    dict_0 = {}
    queue_node_2 = module_0.QueueNode(dict_0)
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    var_1 = queue_0.enqueue(str_0)
    assert len(queue_0) == 1
    none_type_1 = None
    queue_node_4 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_2 = queue_1.__len__()
    assert var_2 == 0
    var_3 = queue_1.peek()
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_4 = queue_2.enqueue(queue_2)
    assert len(queue_2) == 1
    str_1 = 'a,~'
    queue_node_5 = module_0.QueueNode(str_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_6 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_7 = module_0.QueueNode(tuple_0)
    bool_0 = True
    var_5 = queue_3.enqueue(bool_0)
    assert len(queue_3) == 1
    none_type_3 = None
    queue_node_8 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_9 = module_0.QueueNode(none_type_4)
    var_7 = queue_5.enqueue(none_type_3)
    assert len(queue_5) == 1
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0

def test_case_164():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0

def test_case_165():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.peek()
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    queue_node_2 = module_0.QueueNode(none_type_1)
    var_4 = queue_4.clear()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    queue_node_4 = module_0.QueueNode(none_type_2)
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = queue_6.peek()
    str_0 = 'a,~'
    queue_node_6 = module_0.QueueNode(str_0)
    var_8 = queue_6.__str__()
    queue_node_7 = module_0.QueueNode(var_8)
    none_type_4 = None
    queue_node_8 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_9 = module_0.QueueNode(tuple_0)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__str__()
    none_type_5 = None
    queue_node_10 = module_0.QueueNode(none_type_5)
    queue_node_11 = module_0.QueueNode(queue_node_10)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_10 = queue_8.enqueue(queue_8)
    assert len(queue_8) == 1
    var_11 = queue_8.__str__()

def test_case_166():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    dict_0 = {}
    queue_node_2 = module_0.QueueNode(dict_0)
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    var_2 = queue_1.enqueue(str_0)
    assert len(queue_1) == 1
    none_type_1 = None
    queue_node_4 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    var_4 = queue_2.peek()
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_5 = queue_3.__len__()
    assert var_5 == 0
    var_6 = queue_3.peek()
    str_1 = 'a,~'
    queue_node_6 = module_0.QueueNode(str_1)
    var_7 = queue_3.__str__()
    queue_node_7 = module_0.QueueNode(var_7)
    none_type_3 = None
    queue_node_8 = module_0.QueueNode(none_type_3)
    queue_node_9 = module_0.QueueNode(queue_node_8)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_10 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_8 = queue_5.__len__()
    assert var_8 == 0
    var_9 = queue_5.__len__()
    assert var_9 == 0
    var_10 = var_9.__str__()
    assert var_10 == '0'
    none_type_5 = None
    queue_node_11 = module_0.QueueNode(none_type_5)
    tuple_0 = ()
    queue_node_12 = module_0.QueueNode(tuple_0)
    var_11 = queue_0.peek()

def test_case_167():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_3 = queue_4.enqueue(none_type_1)
    assert len(queue_4) == 1
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_4 = queue_6.__str__()
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_5 = queue_8.__len__()
    assert var_5 == 0
    var_6 = queue_8.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    dict_0 = {}
    queue_node_7 = module_0.QueueNode(dict_0)
    var_8 = queue_8.clear()

def test_case_168():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    str_0 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_0)
    dict_0 = {}
    queue_node_3 = module_0.QueueNode(dict_0)
    var_1 = queue_0.__len__()
    assert var_1 == 0

def test_case_169():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    bool_0 = True
    var_0 = queue_0.enqueue(bool_0)
    assert len(queue_0) == 1
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_node_3 = module_0.QueueNode(none_type_1)
    var_3 = queue_2.clear()
    var_4 = queue_2.__str__()

def test_case_170():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    dict_0 = {}
    queue_node_0 = module_0.QueueNode(dict_0)
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_1 = queue_0.enqueue(str_0)
    assert len(queue_0) == 1
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    str_1 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_1)
    queue_node_4 = module_0.QueueNode(queue_node_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_1 = None
    queue_node_5 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_6 = module_0.QueueNode(tuple_0)
    bool_0 = True
    var_5 = queue_3.enqueue(bool_0)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.enqueue(queue_4)
    assert len(queue_4) == 1
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    dict_1 = {}
    queue_node_7 = module_0.QueueNode(dict_1)
    none_type_2 = None
    queue_node_8 = module_0.QueueNode(none_type_2)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    var_8 = queue_7.peek()
    str_2 = 'a,~'
    queue_node_9 = module_0.QueueNode(str_2)
    var_9 = queue_7.__str__()
    queue_node_10 = module_0.QueueNode(var_9)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_10 = queue_4.peek()
    assert len(var_10) == 1

def test_case_171():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = queue_1.peek()
    str_0 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_0)
    var_3 = queue_1.__str__()
    queue_node_3 = module_0.QueueNode(var_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    bool_0 = True
    var_4 = queue_2.enqueue(bool_0)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0

def test_case_172():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.peek()
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = queue_1.peek()
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    str_1 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0

def test_case_173():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    dict_0 = {}
    queue_node_1 = module_0.QueueNode(dict_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.peek()
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.enqueue(queue_2)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    queue_node_3 = module_0.QueueNode(none_type_0)
    var_5 = queue_4.clear()
    var_6 = queue_2.__str__()

def test_case_174():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    dict_0 = {}
    queue_node_3 = module_0.QueueNode(dict_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.enqueue(queue_1)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_0.__str__()

def test_case_175():
    int_0 = 417
    tuple_0 = (int_0, int_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(tuple_0)
    assert len(queue_0) == 1
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    dict_0 = {}
    queue_node_0 = module_0.QueueNode(dict_0)
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_2 = queue_1.enqueue(str_0)
    assert len(queue_1) == 1
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    var_4 = queue_3.enqueue(none_type_0)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    str_1 = 'a,~'
    queue_node_4 = module_0.QueueNode(str_1)
    queue_node_5 = module_0.QueueNode(queue_node_4)
    none_type_2 = None
    queue_node_6 = module_0.QueueNode(none_type_2)
    queue_node_7 = module_0.QueueNode(queue_node_6)
    none_type_3 = None
    queue_node_8 = module_0.QueueNode(none_type_3)
    none_type_4 = None
    queue_node_9 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    queue_node_10 = module_0.QueueNode(none_type_4)
    none_type_5 = None
    queue_node_11 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    none_type_6 = None
    queue_node_12 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_13 = module_0.QueueNode(tuple_1)
    var_7 = queue_6.clear()
    none_type_7 = None
    queue_node_14 = module_0.QueueNode(none_type_7)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__len__()
    assert var_8 == 0
    var_9 = queue_7.peek()
    str_2 = 'a,~'
    queue_node_15 = module_0.QueueNode(str_2)
    var_10 = queue_7.__str__()
    queue_node_16 = module_0.QueueNode(var_10)
    var_11 = queue_0.clear()
    assert len(queue_0) == 0

def test_case_176():
    int_0 = 417
    tuple_0 = (int_0, int_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(tuple_0)
    assert len(queue_0) == 1
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_1 = queue_3.__len__()
    assert var_1 == 0
    dict_0 = {}
    queue_node_0 = module_0.QueueNode(dict_0)
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_2 = queue_3.enqueue(str_0)
    assert len(queue_3) == 1
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    str_1 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_1)
    queue_node_4 = module_0.QueueNode(queue_node_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_1 = None
    queue_node_5 = module_0.QueueNode(none_type_1)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_4 = queue_7.__len__()
    assert var_4 == 0
    var_5 = queue_7.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_6.peek()
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_2 = None
    queue_node_6 = module_0.QueueNode(none_type_2)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_8 = queue_9.__len__()
    assert var_8 == 0
    var_9 = queue_9.__len__()
    assert var_9 == 0
    var_10 = var_9.__str__()
    assert var_10 == '0'
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0
    none_type_3 = None
    queue_node_7 = module_0.QueueNode(none_type_3)
    queue_12 = module_0.Queue()
    assert len(queue_12) == 0
    var_11 = queue_12.__len__()
    assert var_11 == 0
    var_12 = queue_12.__len__()
    assert var_12 == 0
    var_13 = var_12.__str__()
    assert var_13 == '0'
    queue_13 = module_0.Queue()
    assert len(queue_13) == 0
    none_type_4 = None
    queue_node_8 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_9 = module_0.QueueNode(tuple_1)
    bool_0 = True
    var_14 = queue_13.enqueue(bool_0)
    assert len(queue_13) == 1
    queue_14 = module_0.Queue()
    assert len(queue_14) == 0
    var_15 = queue_14.enqueue(queue_14)
    assert len(queue_14) == 1
    queue_node_10 = module_0.QueueNode(var_3)
    assert queue_node_10.data == 0

def test_case_177():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_2 = queue_5.__len__()
    assert var_2 == 0
    var_3 = queue_5.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    var_5 = queue_4.peek()
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0

def test_case_178():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    str_1 = 'a,~'
    queue_node_4 = module_0.QueueNode(str_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_5 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.peek()
    queue_node_6 = module_0.QueueNode(str_0)

def test_case_179():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_node_5 = module_0.QueueNode(queue_node_4)
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_7 = module_0.QueueNode(tuple_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__str__()
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_8 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_9 = module_0.QueueNode(tuple_1)
    bool_0 = True
    var_5 = queue_4.enqueue(bool_0)
    assert len(queue_4) == 1
    none_type_5 = None
    queue_node_10 = module_0.QueueNode(none_type_5)
    tuple_2 = ()
    queue_node_11 = module_0.QueueNode(tuple_2)
    none_type_6 = None
    queue_node_12 = module_0.QueueNode(none_type_6)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    none_type_7 = None
    queue_node_13 = module_0.QueueNode(none_type_7)
    tuple_3 = ()
    queue_node_14 = module_0.QueueNode(tuple_3)
    var_7 = queue_5.clear()
    var_8 = queue_3.__len__()
    assert var_8 == 0

def test_case_180():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.peek()
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    var_6 = queue_5.__str__()
    queue_node_4 = module_0.QueueNode(var_6)
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_node_6 = module_0.QueueNode(queue_node_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.peek()
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_8 = module_0.QueueNode(tuple_0)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__str__()
    dict_0 = {}
    queue_node_9 = module_0.QueueNode(dict_0)
    none_type_5 = None
    queue_node_10 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    var_10 = queue_8.peek()
    var_11 = var_2.__str__()
    assert var_11 == '0'

def test_case_181():
    int_0 = 417
    tuple_0 = (int_0, int_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(tuple_0)
    assert len(queue_0) == 1
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    dict_0 = {}
    queue_node_0 = module_0.QueueNode(dict_0)
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_2 = queue_1.enqueue(str_0)
    assert len(queue_1) == 1
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    tuple_1 = ()
    queue_node_3 = module_0.QueueNode(tuple_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.enqueue(queue_2)
    assert len(queue_2) == 1
    none_type_1 = None
    queue_node_4 = module_0.QueueNode(none_type_1)
    var_4 = queue_0.enqueue(dict_0)
    assert len(queue_0) == 2

def test_case_182():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = queue_2.peek()
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    var_4 = queue_2.__str__()
    queue_node_4 = module_0.QueueNode(var_4)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_5 = queue_3.__len__()
    assert var_5 == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    queue_node_6 = module_0.QueueNode(none_type_3)
    var_7 = queue_4.clear()
    str_1 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_1)
    queue_node_8 = module_0.QueueNode(queue_node_7)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_4 = None
    queue_node_9 = module_0.QueueNode(none_type_4)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__len__()
    assert var_8 == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    var_10 = var_9.__str__()
    assert var_10 == '0'
    var_11 = queue_6.peek()
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_12 = queue_8.__len__()
    assert var_12 == 0
    dict_0 = {}
    queue_node_10 = module_0.QueueNode(dict_0)
    str_2 = 'a,~'
    queue_node_11 = module_0.QueueNode(str_2)
    var_13 = queue_8.enqueue(str_2)
    assert len(queue_8) == 1
    none_type_5 = None
    queue_node_12 = module_0.QueueNode(none_type_5)
    var_14 = queue_7.__str__()

def test_case_183():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_node_2 = module_0.QueueNode(none_type_1)
    var_3 = queue_2.clear()
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    queue_node_4 = module_0.QueueNode(queue_node_3)
    var_4 = queue_0.dequeue()
    assert len(queue_0) == 0
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'queue1.Queue'
    assert len(var_4) == 0

def test_case_184():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0

def test_case_185():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.peek()

def test_case_186():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.peek()
    var_1 = var_0.__str__()

def test_case_187():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0

def test_case_188():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_2 = queue_4.__len__()
    assert var_2 == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'

def test_case_189():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_4 = queue_4.enqueue(none_type_1)
    assert len(queue_4) == 1
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)

def test_case_190():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    with pytest.raises(ValueError):
        queue_1.dequeue()

def test_case_191():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    var_2 = queue_2.enqueue(none_type_2)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    tuple_1 = ()
    queue_node_7 = module_0.QueueNode(tuple_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__str__()
    with pytest.raises(ValueError):
        queue_0.dequeue()

def test_case_192():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    var_6 = queue_5.enqueue(none_type_4)
    assert len(queue_5) == 1
    var_7 = var_4.__str__()
    assert var_7 == '0'

def test_case_193():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    var_5 = queue_4.enqueue(none_type_3)
    assert len(queue_4) == 1
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0

def test_case_194():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__str__()
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0

def test_case_195():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0

def test_case_196():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__str__()
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    var_6 = queue_5.enqueue(none_type_4)
    assert len(queue_5) == 1

def test_case_197():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    tuple_2 = ()
    queue_node_7 = module_0.QueueNode(tuple_2)
    var_2 = queue_1.clear()
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'

def test_case_198():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_4 = queue_4.enqueue(none_type_1)
    assert len(queue_4) == 1
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__str__()
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    with pytest.raises(ValueError):
        queue_2.dequeue()

def test_case_199():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0

def test_case_200():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_3 = queue_6.__len__()
    assert var_3 == 0
    var_4 = queue_6.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    var_6 = queue_5.peek()

def test_case_201():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_0.__str__()

def test_case_202():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_2 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    tuple_1 = ()
    queue_node_7 = module_0.QueueNode(tuple_1)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_7 = queue_8.__len__()
    assert var_7 == 0
    var_8 = queue_8.__len__()
    assert var_8 == 0
    var_9 = var_8.__str__()
    assert var_9 == '0'
    var_10 = queue_7.peek()
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_11 = queue_9.__len__()
    assert var_11 == 0
    none_type_8 = None
    queue_node_10 = module_0.QueueNode(none_type_8)
    tuple_2 = ()
    queue_node_11 = module_0.QueueNode(tuple_2)
    var_12 = queue_9.clear()

def test_case_203():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__str__()

def test_case_204():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    var_4 = queue_4.enqueue(none_type_3)
    assert len(queue_4) == 1
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    tuple_1 = ()
    queue_node_7 = module_0.QueueNode(tuple_1)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__str__()
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_6 = queue_8.__len__()
    assert var_6 == 0
    var_7 = queue_8.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    var_9 = queue_7.peek()

def test_case_205():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)

def test_case_206():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    with pytest.raises(ValueError):
        queue_0.dequeue()

def test_case_207():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    var_5 = queue_4.enqueue(none_type_2)
    assert len(queue_4) == 1
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__str__()
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    none_type_6 = None
    queue_node_7 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_8 = module_0.QueueNode(tuple_1)
    var_8 = queue_6.clear()
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    none_type_8 = None
    queue_node_10 = module_0.QueueNode(none_type_8)
    tuple_2 = ()
    queue_node_11 = module_0.QueueNode(tuple_2)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_9 = None
    queue_node_12 = module_0.QueueNode(none_type_9)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_10 = queue_9.__len__()
    assert var_10 == 0
    var_11 = queue_9.__len__()
    assert var_11 == 0
    var_12 = var_11.__str__()
    assert var_12 == '0'

def test_case_208():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    tuple_1 = ()
    queue_node_3 = module_0.QueueNode(tuple_1)
    with pytest.raises(ValueError):
        queue_0.dequeue()

def test_case_209():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    none_type_5 = None
    queue_node_5 = module_0.QueueNode(none_type_5)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    none_type_6 = None
    queue_node_6 = module_0.QueueNode(none_type_6)
    tuple_0 = ()
    queue_node_7 = module_0.QueueNode(tuple_0)
    var_7 = queue_5.clear()

def test_case_210():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    with pytest.raises(ValueError):
        queue_0.dequeue()

def test_case_211():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_3 = queue_5.__len__()
    assert var_3 == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    var_6 = queue_4.peek()
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.__str__()
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__len__()
    assert var_8 == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    var_9 = queue_8.enqueue(none_type_4)
    assert len(queue_8) == 1

def test_case_212():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_1 = queue_1.enqueue(none_type_1)
    assert len(queue_1) == 1
    str_0 = 'a,~'
    queue_node_4 = module_0.QueueNode(str_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_6 = module_0.QueueNode(tuple_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__str__()
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    tuple_2 = ()
    queue_node_9 = module_0.QueueNode(tuple_2)
    var_4 = queue_4.clear()
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_6 = None
    queue_node_10 = module_0.QueueNode(none_type_6)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_5 = queue_7.__len__()
    assert var_5 == 0
    var_6 = queue_7.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    var_8 = queue_6.peek()
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_8 = None
    queue_node_12 = module_0.QueueNode(none_type_8)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_9 = queue_9.__len__()
    assert var_9 == 0
    var_10 = queue_9.__len__()
    assert var_10 == 0
    var_11 = var_10.__str__()
    assert var_11 == '0'

def test_case_213():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_1 = queue_1.enqueue(none_type_1)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    str_0 = 'a,~'
    queue_node_5 = module_0.QueueNode(str_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    var_8 = queue_5.peek()
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    tuple_1 = ()
    queue_node_10 = module_0.QueueNode(tuple_1)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_10 = queue_8.__str__()
    none_type_8 = None
    queue_node_11 = module_0.QueueNode(none_type_8)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_11 = queue_9.__len__()
    assert var_11 == 0
    none_type_9 = None
    queue_node_12 = module_0.QueueNode(none_type_9)
    tuple_2 = ()
    queue_node_13 = module_0.QueueNode(tuple_2)
    var_12 = queue_9.clear()

def test_case_214():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    var_2 = queue_1.clear()
    with pytest.raises(ValueError):
        queue_1.dequeue()

def test_case_215():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_1 = queue_3.__len__()
    assert var_1 == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    var_4 = queue_2.peek()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__str__()
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    tuple_2 = ()
    queue_node_8 = module_0.QueueNode(tuple_2)
    var_7 = queue_5.clear()
    with pytest.raises(ValueError):
        queue_2.dequeue()

def test_case_216():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'

def test_case_217():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    var_2 = queue_2.enqueue(none_type_2)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    queue_node_6 = module_0.QueueNode(none_type_4)
    str_0 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_0)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_4 = queue_6.__len__()
    assert var_4 == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0

def test_case_218():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    tuple_1 = ()
    queue_node_3 = module_0.QueueNode(tuple_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_1 = queue_4.__len__()
    assert var_1 == 0
    var_2 = queue_4.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    var_4 = queue_3.peek()
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    var_6 = queue_6.enqueue(none_type_3)
    assert len(queue_6) == 1
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_8 = queue_8.__len__()
    assert var_8 == 0
    queue_node_9 = module_0.QueueNode(none_type_6)
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    str_0 = 'a,~'
    queue_node_11 = module_0.QueueNode(str_0)

def test_case_219():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__str__()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    var_5 = queue_3.clear()
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    str_0 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_0)
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    var_7 = queue_5.enqueue(none_type_5)
    assert len(queue_5) == 1
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    tuple_2 = ()
    queue_node_11 = module_0.QueueNode(tuple_2)
    none_type_8 = None
    queue_node_12 = module_0.QueueNode(none_type_8)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_9 = None
    queue_node_13 = module_0.QueueNode(none_type_9)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_9 = queue_10.__len__()
    assert var_9 == 0
    var_10 = queue_10.__len__()
    assert var_10 == 0
    var_11 = var_10.__str__()
    assert var_11 == '0'
    var_12 = queue_9.peek()

def test_case_220():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    var_2 = queue_2.clear()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    var_4 = queue_4.enqueue(none_type_3)
    assert len(queue_4) == 1
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    none_type_6 = None
    queue_node_7 = module_0.QueueNode(none_type_6)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    queue_node_8 = module_0.QueueNode(none_type_6)

def test_case_221():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_0 = queue_3.__len__()
    assert var_0 == 0
    var_1 = queue_3.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_2.peek()
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    var_5 = queue_4.clear()
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    var_10 = queue_8.enqueue(none_type_5)
    assert len(queue_8) == 1
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_11 = queue_9.__len__()
    assert var_11 == 0
    var_12 = queue_3.__len__()
    assert var_12 == 0

def test_case_222():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    var_1 = queue_0.clear()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    var_5 = queue_2.peek()
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    var_7 = queue_5.enqueue(none_type_4)
    assert len(queue_5) == 1
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    str_0 = 'a,~'
    queue_node_8 = module_0.QueueNode(str_0)
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)

def test_case_223():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0

def test_case_224():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()

def test_case_225():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    with pytest.raises(ValueError):
        queue_1.dequeue()

def test_case_226():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    var_2 = queue_1.clear()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    tuple_2 = ()
    queue_node_10 = module_0.QueueNode(tuple_2)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.__str__()
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__len__()
    assert var_8 == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_8 = None
    queue_node_12 = module_0.QueueNode(none_type_8)
    var_9 = queue_8.enqueue(none_type_7)
    assert len(queue_8) == 1
    none_type_9 = None
    queue_node_13 = module_0.QueueNode(none_type_9)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    none_type_10 = None
    queue_node_14 = module_0.QueueNode(none_type_10)
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0
    var_10 = queue_11.__len__()
    assert var_10 == 0
    var_11 = queue_11.__len__()
    assert var_11 == 0
    var_12 = var_11.__str__()
    assert var_12 == '0'
    var_13 = queue_10.peek()
    with pytest.raises(ValueError):
        queue_1.dequeue()

def test_case_227():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_5 = queue_4.enqueue(none_type_1)
    assert len(queue_4) == 1
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)

def test_case_228():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    var_3 = queue_3.clear()
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    var_5 = queue_5.enqueue(none_type_4)
    assert len(queue_5) == 1
    none_type_6 = None
    queue_node_7 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_7 = None
    queue_node_8 = module_0.QueueNode(none_type_7)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_7 = queue_9.__len__()
    assert var_7 == 0
    var_8 = queue_9.__len__()
    assert var_8 == 0
    var_9 = var_8.__str__()
    assert var_9 == '0'
    var_10 = queue_8.peek()

def test_case_229():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__str__()

def test_case_230():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    var_3 = queue_3.enqueue(none_type_2)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_4 = queue_6.__len__()
    assert var_4 == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    none_type_5 = None
    queue_node_5 = module_0.QueueNode(none_type_5)
    tuple_0 = ()
    queue_node_6 = module_0.QueueNode(tuple_0)
    none_type_6 = None
    queue_node_7 = module_0.QueueNode(none_type_6)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0

def test_case_231():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    tuple_2 = ()
    queue_node_6 = module_0.QueueNode(tuple_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_2 = queue_1.__str__()
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    var_4 = queue_3.enqueue(none_type_4)
    assert len(queue_3) == 1
    str_0 = 'a,~'
    queue_node_9 = module_0.QueueNode(str_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_6 = None
    queue_node_10 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    var_8 = queue_5.peek()
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_8 = None
    queue_node_12 = module_0.QueueNode(none_type_8)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    var_10 = queue_8.__len__()
    assert var_10 == 0
    var_11 = var_10.__str__()
    assert var_11 == '0'

def test_case_232():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_2 = queue_2.enqueue(none_type_0)
    assert len(queue_2) == 1
    str_0 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_0)
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_7 = queue_8.__len__()
    assert var_7 == 0
    var_8 = queue_8.__len__()
    assert var_8 == 0
    var_9 = var_8.__str__()
    assert var_9 == '0'
    var_10 = queue_7.peek()
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0

def test_case_233():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()

def test_case_234():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    var_2 = queue_1.clear()
    str_0 = 'a,~'
    queue_node_5 = module_0.QueueNode(str_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    var_6 = queue_3.peek()
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_7 = queue_5.__len__()
    assert var_7 == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    var_8 = queue_6.enqueue(none_type_4)
    assert len(queue_6) == 1
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    tuple_2 = ()
    queue_node_10 = module_0.QueueNode(tuple_2)

def test_case_235():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()

def test_case_236():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    var_4 = queue_3.clear()
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    queue_node_7 = module_0.QueueNode(none_type_4)
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    var_7 = queue_6.enqueue(none_type_5)
    assert len(queue_6) == 1
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    str_0 = 'a,~'
    queue_node_10 = module_0.QueueNode(str_0)
    with pytest.raises(ValueError):
        queue_5.dequeue()

def test_case_237():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    var_6 = queue_3.peek()
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_7 = queue_5.__str__()
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_8 = module_0.QueueNode(tuple_1)
    str_1 = 'a,~'
    queue_node_9 = module_0.QueueNode(str_1)
    none_type_5 = None
    queue_node_10 = module_0.QueueNode(none_type_5)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    queue_node_11 = module_0.QueueNode(none_type_5)

def test_case_238():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0

def test_case_239():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    var_5 = queue_4.clear()
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_6 = module_0.QueueNode(tuple_1)

def test_case_240():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.peek()

def test_case_241():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)

def test_case_242():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_4 = queue_3.enqueue(none_type_1)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    var_8 = queue_5.peek()
    str_0 = 'a,~'
    queue_node_4 = module_0.QueueNode(str_0)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_10 = queue_8.__len__()
    assert var_10 == 0
    queue_node_6 = module_0.QueueNode(none_type_4)
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_11 = queue_9.__len__()
    assert var_11 == 0
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    tuple_0 = ()
    queue_node_9 = module_0.QueueNode(tuple_0)
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    none_type_8 = None
    queue_node_11 = module_0.QueueNode(none_type_8)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_12 = queue_10.__len__()
    assert var_12 == 0
    none_type_9 = None
    queue_node_12 = module_0.QueueNode(none_type_9)
    tuple_1 = ()
    queue_node_13 = module_0.QueueNode(tuple_1)
    var_13 = queue_10.clear()

def test_case_243():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0

def test_case_244():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_1 = queue_1.enqueue(none_type_1)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__str__()
    str_0 = 'a,~'
    queue_node_5 = module_0.QueueNode(str_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_3 = queue_5.__len__()
    assert var_3 == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    tuple_1 = ()
    queue_node_8 = module_0.QueueNode(tuple_1)
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    tuple_2 = ()
    queue_node_11 = module_0.QueueNode(tuple_2)
    var_7 = queue_6.clear()
    str_1 = 'a,~'
    queue_node_12 = module_0.QueueNode(str_1)
    queue_node_13 = module_0.QueueNode(queue_node_12)
    with pytest.raises(ValueError):
        queue_6.dequeue()

def test_case_245():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    queue_node_3 = module_0.QueueNode(none_type_2)
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__len__()
    assert var_8 == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_6 = module_0.QueueNode(tuple_0)
    var_9 = queue_7.clear()
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_10 = queue_9.__len__()
    assert var_10 == 0
    var_11 = queue_9.__len__()
    assert var_11 == 0
    var_12 = var_11.__str__()
    assert var_12 == '0'
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_13 = queue_10.__len__()
    assert var_13 == 0
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0
    none_type_7 = None
    queue_node_9 = module_0.QueueNode(none_type_7)
    var_14 = queue_11.enqueue(none_type_6)
    assert len(queue_11) == 1
    queue_12 = module_0.Queue()
    assert len(queue_12) == 0
    none_type_8 = None
    queue_node_10 = module_0.QueueNode(none_type_8)
    queue_13 = module_0.Queue()
    assert len(queue_13) == 0
    var_15 = queue_13.__len__()
    assert var_15 == 0
    none_type_9 = None
    queue_node_11 = module_0.QueueNode(none_type_9)
    queue_14 = module_0.Queue()
    assert len(queue_14) == 0
    var_16 = queue_14.__len__()
    assert var_16 == 0
    queue_15 = module_0.Queue()
    assert len(queue_15) == 0
    none_type_10 = None
    queue_node_12 = module_0.QueueNode(none_type_10)
    var_17 = queue_15.enqueue(none_type_9)
    assert len(queue_15) == 1
    none_type_11 = None
    queue_node_13 = module_0.QueueNode(none_type_11)

def test_case_246():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0

def test_case_247():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()

def test_case_248():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_0 = None
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    var_2 = queue_2.enqueue(none_type_0)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_3 = queue_5.__len__()
    assert var_3 == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_1.__len__()
    assert var_6 == 0

def test_case_249():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_4.peek()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    var_9 = queue_7.enqueue(none_type_3)
    assert len(queue_7) == 1
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    tuple_0 = ()
    queue_node_7 = module_0.QueueNode(tuple_0)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_10 = queue_8.__str__()
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)

def test_case_250():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0

def test_case_251():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    str_0 = 'a,~'
    queue_node_2 = module_0.QueueNode(str_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__len__()
    assert var_4 == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_7 = queue_5.__len__()
    assert var_7 == 0

def test_case_252():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_6 = module_0.QueueNode(tuple_1)
    var_5 = queue_3.clear()
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    var_7 = queue_5.enqueue(none_type_4)
    assert len(queue_5) == 1
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0

def test_case_253():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    queue_node_2 = module_0.QueueNode(queue_node_1)
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.enqueue(queue_1)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    var_8 = queue_5.peek()
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    var_10 = queue_8.enqueue(none_type_5)
    assert len(queue_8) == 1
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    str_1 = 'a,~'
    queue_node_10 = module_0.QueueNode(str_1)
    with pytest.raises(ValueError):
        queue_7.dequeue()

def test_case_254():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.peek()

def test_case_255():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.enqueue(queue_3)
    assert len(queue_3) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    var_4 = queue_5.enqueue(none_type_2)
    assert len(queue_5) == 1
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_5 = None
    queue_node_5 = module_0.QueueNode(none_type_5)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_6 = queue_8.__len__()
    assert var_6 == 0
    var_7 = queue_8.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    none_type_6 = None
    queue_node_6 = module_0.QueueNode(none_type_6)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_9 = queue_9.__len__()
    assert var_9 == 0
    queue_node_7 = module_0.QueueNode(none_type_6)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_10 = queue_10.__len__()
    assert var_10 == 0

def test_case_256():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    str_0 = 'a,~'
    queue_node_5 = module_0.QueueNode(str_0)
    queue_node_6 = module_0.QueueNode(queue_node_5)
    none_type_3 = None
    queue_node_7 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    none_type_4 = None
    queue_node_8 = module_0.QueueNode(none_type_4)
    str_1 = 'a,~'
    queue_node_9 = module_0.QueueNode(str_1)

def test_case_257():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_4 = module_0.QueueNode(tuple_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_2 = queue_1.__str__()
    str_0 = 'a,~'
    queue_node_5 = module_0.QueueNode(str_0)
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    var_4 = queue_3.enqueue(none_type_3)
    assert len(queue_3) == 1
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    tuple_2 = ()
    queue_node_9 = module_0.QueueNode(tuple_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_6 = None
    queue_node_10 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    var_8 = queue_5.peek()
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_7 = None
    queue_node_11 = module_0.QueueNode(none_type_7)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    var_10 = queue_8.__len__()
    assert var_10 == 0
    var_11 = var_10.__str__()
    assert var_11 == '0'
    str_1 = 'a,~'
    queue_node_12 = module_0.QueueNode(str_1)
    queue_node_13 = module_0.QueueNode(queue_node_12)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_12 = queue_9.__len__()
    assert var_12 == 0
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0

def test_case_258():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    str_1 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_1)
    queue_node_2 = module_0.QueueNode(queue_node_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_3 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    none_type_1 = None
    queue_node_4 = module_0.QueueNode(none_type_1)
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.enqueue(queue_4)
    assert len(queue_4) == 1
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_7 = module_0.QueueNode(tuple_0)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_4 = None
    queue_node_8 = module_0.QueueNode(none_type_4)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_6 = queue_7.__len__()
    assert var_6 == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0

def test_case_259():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.__len__()
    assert var_4 == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__str__()
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    var_10 = queue_9.enqueue(none_type_4)
    assert len(queue_9) == 1
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    tuple_1 = ()

def test_case_260():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_6 = module_0.QueueNode(tuple_1)
    var_5 = queue_3.clear()
    str_0 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_0)
    queue_node_8 = module_0.QueueNode(queue_node_7)
    none_type_5 = None
    queue_node_9 = module_0.QueueNode(none_type_5)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_7 = queue_5.enqueue(queue_5)
    assert len(queue_5) == 1

def test_case_261():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.peek()
    var_1 = var_0.__str__()
    var_2 = var_1.__str__()
    var_3 = var_2.__len__()

def test_case_262():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_2.enqueue(none_type_0)
    assert len(queue_2) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    tuple_0 = ()
    queue_node_4 = module_0.QueueNode(tuple_0)
    var_3 = queue_3.clear()
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_4 = queue_6.__len__()
    assert var_4 == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    var_6 = var_5.__str__()
    assert var_6 == '0'
    var_7 = queue_5.peek()
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    none_type_6 = None
    queue_node_7 = module_0.QueueNode(none_type_6)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_8 = queue_7.__len__()
    assert var_8 == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_7 = None
    queue_node_8 = module_0.QueueNode(none_type_7)
    var_9 = queue_8.enqueue(none_type_6)
    assert len(queue_8) == 1
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0

def test_case_263():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__str__()
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_1 = queue_4.__len__()
    assert var_1 == 0
    var_2 = queue_4.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    var_4 = queue_3.peek()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_5 = module_0.QueueNode(tuple_1)
    var_6 = queue_5.clear()
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_4 = None
    queue_node_6 = module_0.QueueNode(none_type_4)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_7 = queue_7.__len__()
    assert var_7 == 0
    var_8 = queue_7.__len__()
    assert var_8 == 0
    var_9 = var_8.__str__()
    assert var_9 == '0'
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    str_0 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_0)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_10 = queue_9.enqueue(queue_9)
    assert len(queue_9) == 1
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_11 = queue_10.__len__()
    assert var_11 == 0

def test_case_264():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    var_1 = queue_1.enqueue(none_type_1)
    assert len(queue_1) == 1
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_2 = queue_4.__len__()
    assert var_2 == 0
    var_3 = queue_4.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    var_5 = queue_3.peek()
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    var_7 = queue_5.peek()
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0

def test_case_265():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    var_4 = queue_3.clear()

def test_case_266():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_2 = queue_1.__len__()
    assert var_2 == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_3 = queue_2.enqueue(none_type_1)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0

def test_case_267():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()

def test_case_268():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    var_1 = queue_1.enqueue(none_type_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__str__()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.enqueue(queue_4)
    assert len(queue_4) == 1
    none_type_5 = None
    queue_node_6 = module_0.QueueNode(none_type_5)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = queue_5.peek()
    none_type_6 = None
    queue_node_7 = module_0.QueueNode(none_type_6)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = queue_6.peek()
    str_0 = 'a,~'
    queue_node_8 = module_0.QueueNode(str_0)
    var_9 = queue_6.__str__()
    queue_node_9 = module_0.QueueNode(var_9)
    none_type_7 = None
    queue_node_10 = module_0.QueueNode(none_type_7)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_10 = queue_7.__len__()
    assert var_10 == 0
    queue_node_11 = module_0.QueueNode(none_type_7)

def test_case_269():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = queue_1.peek()
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.enqueue(queue_2)
    assert len(queue_2) == 1
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    tuple_1 = ()
    queue_node_6 = module_0.QueueNode(tuple_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__str__()

def test_case_270():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_2 = queue_0.__str__()
    queue_node_2 = module_0.QueueNode(var_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    var_4 = queue_2.__len__()
    assert var_4 == 0
    var_5 = var_4.__str__()
    assert var_5 == '0'
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_7 = queue_5.__len__()
    assert var_7 == 0
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    var_8 = queue_6.enqueue(none_type_4)
    assert len(queue_6) == 1
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_9 = queue_7.__len__()
    assert var_9 == 0

def test_case_271():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0

def test_case_272():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    str_0 = 'a,~'
    queue_node_3 = module_0.QueueNode(str_0)
    queue_node_4 = module_0.QueueNode(queue_node_3)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_5 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    var_3 = queue_2.__len__()
    assert var_3 == 0
    var_4 = var_3.__str__()
    assert var_4 == '0'
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    tuple_1 = ()
    queue_node_7 = module_0.QueueNode(tuple_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_5 = queue_3.enqueue(queue_3)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_8 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    var_9 = queue_5.peek()

def test_case_273():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.clear()
    var_1 = var_0.__str__()

def test_case_274():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    var_5 = queue_3.clear()
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    var_9 = var_8.__str__()
    assert var_9 == '0'
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    str_0 = 'a,~'
    queue_node_6 = module_0.QueueNode(str_0)
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_10 = queue_9.__len__()
    assert var_10 == 0
    var_11 = queue_9.peek()
    none_type_6 = None
    queue_node_8 = module_0.QueueNode(none_type_6)
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    var_12 = queue_10.__len__()
    assert var_12 == 0
    queue_node_9 = module_0.QueueNode(none_type_6)

def test_case_275():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = var_0.__str__()
    assert var_1 == '0'

def test_case_276():
    dict_0 = {}
    queue_node_0 = module_0.QueueNode(dict_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_0 = None
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_1 = queue_3.__len__()
    assert var_1 == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    var_4 = queue_2.peek()
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    queue_node_3 = module_0.QueueNode(none_type_1)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_6 = queue_6.__len__()
    assert var_6 == 0
    var_7 = queue_6.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    str_0 = 'a,~'
    queue_node_5 = module_0.QueueNode(str_0)
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    var_9 = queue_8.__len__()
    assert var_9 == 0
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    var_10 = queue_9.enqueue(none_type_4)
    assert len(queue_9) == 1
    queue_10 = module_0.Queue()
    assert len(queue_10) == 0
    none_type_6 = None
    queue_node_9 = module_0.QueueNode(none_type_6)
    queue_11 = module_0.Queue()
    assert len(queue_11) == 0
    var_11 = queue_11.__len__()
    assert var_11 == 0
    var_12 = queue_11.__len__()
    assert var_12 == 0
    var_13 = var_12.__str__()
    assert var_13 == '0'

def test_case_277():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    bool_0 = True
    var_0 = queue_0.enqueue(bool_0)
    assert len(queue_0) == 1
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    tuple_1 = ()
    queue_node_3 = module_0.QueueNode(tuple_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__str__()
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_node_5 = module_0.QueueNode(queue_node_4)
    none_type_3 = None
    queue_node_6 = module_0.QueueNode(none_type_3)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    var_3 = queue_3.enqueue(none_type_3)
    assert len(queue_3) == 1
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0

def test_case_278():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    var_4 = queue_4.enqueue(none_type_2)
    assert len(queue_4) == 1

def test_case_279():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0

def test_case_280():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_2 = queue_0.__str__()
    queue_node_2 = module_0.QueueNode(var_2)
    dict_0 = {}
    queue_node_3 = module_0.QueueNode(dict_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_1 = None
    queue_node_4 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    bool_0 = True
    var_3 = queue_1.enqueue(bool_0)
    assert len(queue_1) == 1
    none_type_2 = None
    queue_node_6 = module_0.QueueNode(none_type_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_4 = queue_2.__len__()
    assert var_4 == 0
    var_5 = queue_2.peek()
    str_1 = 'a,~'
    queue_node_7 = module_0.QueueNode(str_1)
    queue_node_8 = module_0.QueueNode(queue_node_7)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    none_type_3 = None
    queue_node_9 = module_0.QueueNode(none_type_3)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_6 = queue_4.__len__()
    assert var_6 == 0
    var_7 = queue_4.__len__()
    assert var_7 == 0
    var_8 = var_7.__str__()
    assert var_8 == '0'
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_4 = None
    queue_node_10 = module_0.QueueNode(none_type_4)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_9 = queue_6.__len__()
    assert var_9 == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_5 = None
    queue_node_11 = module_0.QueueNode(none_type_5)
    var_10 = queue_7.enqueue(none_type_4)
    assert len(queue_7) == 1
    queue_8 = module_0.Queue()
    assert len(queue_8) == 0
    none_type_6 = None
    queue_node_12 = module_0.QueueNode(none_type_6)
    tuple_1 = ()
    queue_node_13 = module_0.QueueNode(tuple_1)
    queue_9 = module_0.Queue()
    assert len(queue_9) == 0
    var_11 = queue_9.__str__()

def test_case_281():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()

def test_case_282():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    var_4 = queue_2.__str__()

def test_case_283():
    str_0 = 'a,~'
    queue_node_0 = module_0.QueueNode(str_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    none_type_1 = None
    queue_node_4 = module_0.QueueNode(none_type_1)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    var_1 = queue_0.peek()
    str_1 = 'a,~'
    queue_node_5 = module_0.QueueNode(str_1)
    var_2 = queue_0.__str__()
    queue_node_6 = module_0.QueueNode(var_2)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_2 = None
    queue_node_7 = module_0.QueueNode(none_type_2)
    tuple_1 = ()
    queue_node_8 = module_0.QueueNode(tuple_1)
    bool_0 = True
    var_3 = queue_1.enqueue(bool_0)
    assert len(queue_1) == 1
    str_2 = 'a,~'
    queue_node_9 = module_0.QueueNode(str_2)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_4 = queue_2.enqueue(queue_2)
    assert len(queue_2) == 1
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_5 = queue_3.__len__()
    assert var_5 == 0
    dict_0 = {}
    queue_node_10 = module_0.QueueNode(dict_0)
    with pytest.raises(ValueError):
        queue_3.dequeue()

def test_case_284():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__str__()

def test_case_285():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_2 = module_0.QueueNode(tuple_0)
    var_1 = queue_0.clear()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_2 = queue_1.enqueue(queue_1)
    assert len(queue_1) == 1

def test_case_286():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.peek()

def test_case_287():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.clear()

def test_case_288():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    queue_node_1 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_1 = queue_3.__len__()
    assert var_1 == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    var_3 = var_2.__str__()
    assert var_3 == '0'
    var_4 = queue_2.peek()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.__len__()
    assert var_5 == 0
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_3 = None
    queue_node_4 = module_0.QueueNode(none_type_3)
    var_6 = queue_5.enqueue(none_type_2)
    assert len(queue_5) == 1
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_7 = queue_7.enqueue(queue_7)
    assert len(queue_7) == 1
    none_type_4 = None
    queue_node_5 = module_0.QueueNode(none_type_4)
    queue_node_6 = module_0.QueueNode(queue_node_5)
    none_type_5 = None
    queue_node_7 = module_0.QueueNode(none_type_5)
    str_0 = 'a,~'
    queue_node_8 = module_0.QueueNode(str_0)

def test_case_289():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_0 = queue_2.__len__()
    assert var_0 == 0
    var_1 = queue_2.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    var_3 = queue_1.peek()
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    tuple_0 = ()
    queue_node_3 = module_0.QueueNode(tuple_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_4 = queue_4.__str__()
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_node_5 = module_0.QueueNode(queue_node_4)

def test_case_290():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    bool_0 = True
    var_1 = queue_1.enqueue(bool_0)
    assert len(queue_1) == 1
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)

def test_case_291():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.clear()

def test_case_292():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_3 = queue_3.__len__()
    assert var_3 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_2 = None
    queue_node_2 = module_0.QueueNode(none_type_2)
    var_4 = queue_4.enqueue(none_type_1)
    assert len(queue_4) == 1
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    none_type_3 = None
    queue_node_3 = module_0.QueueNode(none_type_3)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_5 = queue_6.__len__()
    assert var_5 == 0
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    none_type_4 = None
    queue_node_4 = module_0.QueueNode(none_type_4)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)
    bool_0 = True
    var_6 = queue_7.enqueue(bool_0)
    assert len(queue_7) == 1
    var_7 = queue_3.clear()

def test_case_293():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__len__()
    assert var_0 == 0
    dict_0 = {}
    queue_node_0 = module_0.QueueNode(dict_0)
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)
    var_1 = queue_0.enqueue(str_0)
    assert len(queue_0) == 1
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    none_type_0 = None
    queue_node_2 = module_0.QueueNode(none_type_0)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_2 = queue_3.__len__()
    assert var_2 == 0
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_1 = None
    queue_node_3 = module_0.QueueNode(none_type_1)
    var_3 = queue_4.enqueue(none_type_0)
    assert len(queue_4) == 1
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_4 = queue_5.enqueue(queue_5)
    assert len(queue_5) == 1
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    tuple_0 = ()
    queue_node_5 = module_0.QueueNode(tuple_0)

def test_case_294():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_3 = queue_2.enqueue(queue_2)
    assert len(queue_2) == 1
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    int_0 = 417
    tuple_0 = (int_0, int_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    var_5 = queue_4.enqueue(tuple_0)
    assert len(queue_4) == 1

def test_case_295():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.__str__()
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    var_2 = queue_2.__len__()
    assert var_2 == 0
    queue_node_3 = module_0.QueueNode(none_type_1)
    var_3 = queue_2.clear()
    none_type_2 = None
    queue_node_4 = module_0.QueueNode(none_type_2)
    queue_3 = module_0.Queue()
    assert len(queue_3) == 0
    var_4 = queue_3.__len__()
    assert var_4 == 0
    none_type_3 = None
    queue_node_5 = module_0.QueueNode(none_type_3)
    dict_0 = {}
    queue_node_6 = module_0.QueueNode(dict_0)
    queue_4 = module_0.Queue()
    assert len(queue_4) == 0
    none_type_4 = None
    queue_node_7 = module_0.QueueNode(none_type_4)
    queue_5 = module_0.Queue()
    assert len(queue_5) == 0
    var_5 = queue_5.__len__()
    assert var_5 == 0
    var_6 = queue_5.__len__()
    assert var_6 == 0
    var_7 = var_6.__str__()
    assert var_7 == '0'
    none_type_5 = None
    queue_node_8 = module_0.QueueNode(none_type_5)
    queue_6 = module_0.Queue()
    assert len(queue_6) == 0
    var_8 = queue_6.__len__()
    assert var_8 == 0
    var_9 = queue_6.peek()
    str_0 = 'a,~'
    queue_node_9 = module_0.QueueNode(str_0)
    var_10 = queue_6.__str__()
    queue_node_10 = module_0.QueueNode(var_10)
    queue_7 = module_0.Queue()
    assert len(queue_7) == 0
    var_11 = queue_7.peek()

def test_case_296():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_node_1 = module_0.QueueNode(queue_node_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    with pytest.raises(ValueError):
        queue_0.dequeue()

def test_case_297():
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_0 = queue_1.__len__()
    assert var_0 == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = var_1.__str__()
    assert var_2 == '0'
    queue_2 = module_0.Queue()
    assert len(queue_2) == 0
    str_0 = 'a,~'
    queue_node_1 = module_0.QueueNode(str_0)

def test_case_298():
    int_0 = 417
    tuple_0 = (int_0, int_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(tuple_0)
    assert len(queue_0) == 1
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    none_type_1 = None
    queue_node_1 = module_0.QueueNode(none_type_1)
    tuple_1 = ()
    queue_node_2 = module_0.QueueNode(tuple_1)
    var_2 = queue_1.clear()
    none_type_2 = None
    queue_node_3 = module_0.QueueNode(none_type_2)
    tuple_2 = ()
    queue_node_4 = module_0.QueueNode(tuple_2)

def test_case_299():
    none_type_0 = None
    queue_node_0 = module_0.QueueNode(none_type_0)
    tuple_0 = ()
    queue_node_1 = module_0.QueueNode(tuple_0)
    queue_0 = module_0.Queue()
    assert len(queue_0) == 0
    var_0 = queue_0.enqueue(queue_0)
    assert len(queue_0) == 1
    none_type_1 = None
    queue_node_2 = module_0.QueueNode(none_type_1)
    queue_1 = module_0.Queue()
    assert len(queue_1) == 0
    var_1 = queue_1.__len__()
    assert var_1 == 0
    var_2 = queue_1.peek()
    dict_0 = {}
    queue_node_3 = module_0.QueueNode(dict_0)
