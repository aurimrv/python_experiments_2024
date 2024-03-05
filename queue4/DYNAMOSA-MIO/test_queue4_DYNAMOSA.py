#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue4/DYNAMOSA/test_queue4.py.orig
import pytest
import queue4 as module_0

def test_case_0():
    complex_0 = 1256.54 - 1026.303899j
    float_0 = -335.0
    tuple_0 = (float_0,)
    queue_0 = module_0.Queue(tuple_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    var_0 = queue_0.enqueue(complex_0)

def test_case_1():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_2():
    float_0 = 382.59
    int_0 = -868
    double_linked_list_0 = module_0.DoubleLinkedList(int_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_0.push(float_0)

def test_case_3():
    node_0 = module_0.Node()
    double_linked_list_0 = module_0.DoubleLinkedList(node_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_0.append(double_linked_list_0)
    var_1 = double_linked_list_0.remove(double_linked_list_0)

def test_case_4():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.pop()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue4.DoubleLinkedList'
    assert var_1.head is None
    assert var_1.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.pop()

def test_case_5():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.shift()

def test_case_6():
    int_0 = -868
    double_linked_list_0 = module_0.DoubleLinkedList(int_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_0.shift()
    assert var_0 == -868
    assert double_linked_list_0.tail is None
    double_linked_list_1 = module_0.DoubleLinkedList(int_0)

def test_case_7():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(ValueError):
        double_linked_list_0.remove(double_linked_list_0)

def test_case_8():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    var_0 = queue_0.peek()

def test_case_9():
    node_0 = module_0.Node()

def test_case_10():
    node_0 = module_0.Node()
    bool_0 = False
    var_0 = node_0.__repr__()
    assert var_0 == 'Value: None'
    node_1 = module_0.Node(next_node=bool_0, prev=bool_0)
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'

def test_case_11():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'

def test_case_12():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    var_0 = queue_0.peek()
    var_1 = queue_0.enqueue(var_0)
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_13():
    int_0 = -195
    node_0 = module_0.Node(next_node=int_0)
    none_type_0 = None
    queue_0 = module_0.Queue(none_type_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'

def test_case_14():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    var_0 = queue_0.size()
    assert var_0 == 0
    var_1 = queue_0.size()
    assert var_1 == 0
    var_2 = queue_0.size()
    assert var_2 == 0

def test_case_15():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    var_0 = queue_0.peek()
    int_0 = -864
    double_linked_list_0 = module_0.DoubleLinkedList(int_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.append(double_linked_list_0)
    var_2 = var_1.__repr__()
    var_3 = double_linked_list_0.shift()
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(var_3.head).__module__}.{type(var_3.head).__qualname__}' == 'queue4.Node'
    assert f'{type(var_3.tail).__module__}.{type(var_3.tail).__qualname__}' == 'queue4.Node'
    var_4 = double_linked_list_0.remove(int_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    assert var_3.head is None
    assert var_3.tail is None
    double_linked_list_1 = module_0.DoubleLinkedList()

def test_case_16():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    node_0 = module_0.Node()
    double_linked_list_0 = module_0.DoubleLinkedList(node_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(double_linked_list_0)

def test_case_17():
    dict_0 = {}
    node_0 = module_0.Node()
    double_linked_list_0 = module_0.DoubleLinkedList(node_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    str_0 = '3<}DOM;<l\rvp}?E'
    var_0 = double_linked_list_0.push(str_0)
    var_1 = double_linked_list_0.pop()
    assert var_1 == '3<}DOM;<l\rvp}?E'
    double_linked_list_1 = module_0.DoubleLinkedList()
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None

def test_case_18():
    node_0 = module_0.Node()
    double_linked_list_0 = module_0.DoubleLinkedList(node_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_0.remove(node_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_19():
    int_0 = -839
    double_linked_list_0 = module_0.DoubleLinkedList(int_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_0.append(double_linked_list_0)
    double_linked_list_1 = module_0.DoubleLinkedList(int_0)
    assert f'{type(double_linked_list_1.head).__module__}.{type(double_linked_list_1.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.remove(int_0)
    double_linked_list_2 = module_0.DoubleLinkedList()

def test_case_20():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    queue_1 = module_0.Queue()
    queue_2 = module_0.Queue(queue_0)
    assert f'{type(queue_2).__module__}.{type(queue_2).__qualname__}' == 'queue4.Queue'
    var_0 = queue_2.dequeue()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue4.Queue'
    var_1 = var_0.peek()
    var_2 = var_0.enqueue(queue_0)
    int_0 = -4252
    double_linked_list_0 = module_0.DoubleLinkedList(int_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_3 = double_linked_list_0.push(var_2)
    double_linked_list_1 = module_0.DoubleLinkedList(int_0)
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'queue4.Node'
    var_4 = double_linked_list_0.append(var_1)
    var_5 = double_linked_list_0.remove(int_0)
    double_linked_list_2 = module_0.DoubleLinkedList()
    with pytest.raises(IndexError):
        double_linked_list_2.pop()
