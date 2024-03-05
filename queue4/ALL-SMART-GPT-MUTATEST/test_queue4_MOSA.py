#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue4/MOSA/test_queue4.py.orig
import pytest
import queue4 as module_0

def test_case_0():
    bytes_0 = b'\xaf\xc9-\x02\xb2"&\x0e\xaa\x171\xfd\x00'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    none_type_0 = None
    var_0 = double_linked_list_0.append(none_type_0)
    var_1 = double_linked_list_0.remove(none_type_0)

def test_case_1():
    dict_0 = {}
    node_0 = module_0.Node()
    double_linked_list_0 = module_0.DoubleLinkedList(node_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_0.pop()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue4.Node'
    assert var_0.data is None
    assert var_0.next is None
    assert var_0.prev is None
    with pytest.raises(ValueError):
        double_linked_list_0.remove(dict_0)

def test_case_2():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_3():
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

def test_case_4():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.pop()

def test_case_5():
    bytes_0 = b'\xaf\xc9-\x02\xb2"&\x0e\xfd\x00'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    none_type_0 = None
    var_0 = double_linked_list_0.append(none_type_0)
    var_1 = var_0.__repr__()
    var_2 = double_linked_list_0.remove(none_type_0)
    var_3 = double_linked_list_0.shift()
    assert var_3 == 175
    with pytest.raises(ValueError):
        double_linked_list_0.remove(none_type_0)

def test_case_6():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.shift()

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
    var_0 = node_0.__repr__()
    assert var_0 == 'Value: None'
    double_linked_list_0 = module_0.DoubleLinkedList(node_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    double_linked_list_1 = module_0.DoubleLinkedList()
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None
    with pytest.raises(ValueError):
        double_linked_list_1.remove(node_0)

def test_case_11():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'

def test_case_12():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    var_0 = queue_0.peek()
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_1 = queue_0.enqueue(double_linked_list_0)
    double_linked_list_1 = module_0.DoubleLinkedList()
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None

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
    node_0 = module_0.Node()
    double_linked_list_0 = module_0.DoubleLinkedList(node_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_0.pop()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue4.Node'
    assert var_0.data is None
    assert var_0.next is None
    assert var_0.prev is None
    double_linked_list_1 = module_0.DoubleLinkedList(node_0)
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'queue4.Node'
    var_1 = double_linked_list_1.shift()
    assert double_linked_list_1.tail is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue4.Node'
    assert var_1.data is None
    assert var_1.next is None
    assert var_1.prev is None

def test_case_16():
    dict_0 = {}
    node_0 = module_0.Node()
    double_linked_list_0 = module_0.DoubleLinkedList(node_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    var_0 = module_0.DoubleLinkedList()
    assert var_0.head is None
    assert var_0.tail is None
    with pytest.raises(ValueError):
        double_linked_list_0.remove(dict_0)

def test_case_17():
    bytes_0 = b'\xaf\xc9-\x02\xb2"&\x0e\xfd\x00'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    double_linked_list_1 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_1).__module__}.{type(double_linked_list_1).__qualname__}' == 'queue4.DoubleLinkedList'
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None
    none_type_0 = None
    var_0 = double_linked_list_0.append(none_type_0)
    var_1 = var_0.__repr__()
    var_2 = double_linked_list_0.pop()
    assert var_2 == 0
    var_3 = double_linked_list_0.remove(none_type_0)

def test_case_18():
    dict_0 = {}
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    node_0 = module_0.Node()
    double_linked_list_0 = module_0.DoubleLinkedList(node_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    double_linked_list_1 = module_0.DoubleLinkedList(queue_0)
    assert f'{type(double_linked_list_1.head).__module__}.{type(double_linked_list_1.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'queue4.Node'
    var_0 = double_linked_list_0.remove(node_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_1 = module_0.Queue(dict_0)
    float_0 = 1396.51
    double_linked_list_2 = module_0.DoubleLinkedList(float_0)
    assert f'{type(double_linked_list_2.tail).__module__}.{type(double_linked_list_2.tail).__qualname__}' == 'queue4.Node'
    with pytest.raises(ValueError):
        double_linked_list_2.remove(double_linked_list_0)

def test_case_19():
    bytes_0 = b'\xaf\xc9-\x02\xb2"&\x0e\xfd\x00'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    none_type_0 = None
    var_0 = double_linked_list_0.append(none_type_0)
    var_1 = double_linked_list_0.append(none_type_0)
    var_2 = var_1.__repr__()
    var_3 = double_linked_list_0.remove(none_type_0)
    var_4 = double_linked_list_0.shift()
    with pytest.raises(ValueError):
        double_linked_list_0.remove(none_type_0)

def test_case_20():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'queue4.Queue'
    str_0 = 'U.n@aoHRlv:cx}!'
    bytes_0 = b'\xaf\xc9-\x02\xb2"&\x0e\xfd\x00'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'queue4.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'queue4.Node'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'queue4.Node'
    none_type_0 = None
    var_0 = double_linked_list_0.append(none_type_0)
    var_1 = double_linked_list_0.push(var_0)
    var_2 = var_0.__repr__()
    var_3 = double_linked_list_0.remove(none_type_0)
    with pytest.raises(ValueError):
        double_linked_list_0.remove(str_0)
