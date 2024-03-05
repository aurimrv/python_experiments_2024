#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue4/WHOLE_SUITE/test_queue4.py.orig
import pytest
import queue4 as module_0

def test_case_0():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    var_0 = queue_0.peek()
    var_1 = queue_0.peek()

def test_case_1():
    bytes_0 = b'\x0c\x9f*\xec'
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(bytes_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.append(bytes_0)

def test_case_2():
    none_type_0 = None
    double_linked_list_0 = module_0.DoubleLinkedList(none_type_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    double_linked_list_1 = module_0.DoubleLinkedList(none_type_0)
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None
    with pytest.raises(IndexError):
        double_linked_list_1.shift()

def test_case_3():
    bool_0 = False
    set_0 = {bool_0}
    node_0 = module_0.Node(set_0)
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'

def test_case_4():
    node_0 = module_0.Node()
    bool_0 = False
    var_0 = node_0.__repr__()
    assert var_0 == 'Value: None'

def test_case_5():
    bool_0 = False
    queue_0 = module_0.Queue(bool_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    var_0 = queue_0.enqueue(queue_0)
    var_1 = queue_0.dequeue()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue4.Queue'
    var_2 = queue_0.size()
    assert var_2 == 0
    queue_1 = module_0.Queue()

def test_case_6():
    bool_0 = True
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    none_type_0 = None
    var_0 = double_linked_list_0.push(bool_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(none_type_0)

def test_case_7():
    tuple_0 = ()
    bytes_0 = b'\xe8\xd6\x1f\xb2\xa07\xcfn1=J\xbd'
    dict_0 = {bytes_0: tuple_0, bytes_0: bytes_0}
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    node_0 = module_0.Node(dict_0, tuple_0)
    var_0 = double_linked_list_0.pop()
    assert var_0 == 189
    queue_0 = module_0.Queue(tuple_0)
    var_1 = double_linked_list_0.shift()
    assert var_1 == 232

def test_case_8():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.remove(double_linked_list_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(ValueError):
        double_linked_list_0.remove(double_linked_list_0)

def test_case_9():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    none_type_0 = None
    var_0 = double_linked_list_0.push(none_type_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.push(double_linked_list_0)
    var_2 = double_linked_list_0.remove(double_linked_list_0)
    none_type_1 = None
    var_3 = double_linked_list_0.shift()
    assert double_linked_list_0.tail is None

def test_case_10():
    int_0 = -2937
    double_linked_list_0 = module_0.DoubleLinkedList(int_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    int_1 = -2380
    double_linked_list_1 = module_0.DoubleLinkedList(int_1)
    assert f'{type(double_linked_list_1.head).__module__}.{type(double_linked_list_1.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_1.pop()
    assert var_0 == -2380
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None
    with pytest.raises(IndexError):
        double_linked_list_1.pop()

def test_case_11():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.push(var_0)
    var_2 = double_linked_list_0.remove(double_linked_list_0)
    var_3 = double_linked_list_0.push(double_linked_list_0)

def test_case_12():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_0.push(var_0)
    var_2 = double_linked_list_0.remove(double_linked_list_0)
    var_3 = double_linked_list_0.push(double_linked_list_0)
