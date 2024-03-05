#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree3/WHOLE_SUITE/test_binarySearchTree3.py.orig
import pytest
import binarySearchTree3 as module_0

def test_case_0():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.pre_order()
    queue_0 = module_0.Queue(var_1)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_1():
    node_d_l_l_0 = module_0.NodeDLL()
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    node_d_l_l_1 = module_0.NodeDLL(node_d_l_l_0)
    var_0 = node_d_l_l_0.__repr__()
    assert var_0 == 'Value: None'
    with pytest.raises(IndexError):
        double_linked_list_0.pop()

def test_case_2():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.delete(queue_0)

def test_case_3():
    int_0 = -1638
    double_linked_list_0 = module_0.DoubleLinkedList(int_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    double_linked_list_1 = module_0.DoubleLinkedList()
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_1)
    var_1 = double_linked_list_0.remove(int_0)
    var_2 = var_0.__repr__()

def test_case_4():
    int_0 = -1638
    double_linked_list_0 = module_0.DoubleLinkedList(int_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    double_linked_list_1 = module_0.DoubleLinkedList()
    assert double_linked_list_1.head is None
    assert double_linked_list_1.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_1)
    var_1 = double_linked_list_0.remove(int_0)
    var_2 = var_0.__repr__()

def test_case_5():
    int_0 = -1652
    double_linked_list_0 = module_0.DoubleLinkedList(int_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_0 = double_linked_list_0.shift()
    assert var_0 == -1652
    assert double_linked_list_0.tail is None
    node_d_l_l_0 = module_0.NodeDLL(int_0)
    var_1 = node_d_l_l_0.__repr__()
    assert var_1 == 'Value: -1652'

def test_case_6():
    bytes_0 = b'\xd0\x08\x1b$\xda'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.in_order()
    var_1 = bst_0.depth()
    assert var_1 == 4
    var_2 = bst_0.balance()
    assert var_2 == 2
    double_linked_list_0 = module_0.DoubleLinkedList(var_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'

def test_case_7():
    bytes_0 = b'5\x98{\xa7\x1f8CA\x8cr\x06\x98\x0bY\xad'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_0 = double_linked_list_0.pop()
    assert var_0 == 173
    var_1 = double_linked_list_0.shift()
    assert var_1 == 53
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(var_0)

def test_case_8():
    str_0 = 'iy}'
    double_linked_list_0 = module_0.DoubleLinkedList(str_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(double_linked_list_0)

def test_case_9():
    complex_0 = 2055.829 + 809.794j
    double_linked_list_0 = module_0.DoubleLinkedList(complex_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_0 = double_linked_list_0.push(double_linked_list_0)

def test_case_10():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.remove(double_linked_list_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(ValueError):
        double_linked_list_0.remove(double_linked_list_0)

def test_case_11():
    bool_0 = True
    queue_0 = module_0.Queue(bool_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.enqueue(queue_0)
    var_1 = queue_0.peek()
    assert var_1 is True
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_2 = queue_0.size()
    assert var_2 == 2
    var_3 = bst_0.depth()
    assert var_3 == 0
    var_4 = bst_0.depth()
    assert var_4 == 0

def test_case_12():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.shift()

def test_case_13():
    none_type_0 = None
    node_d_l_l_0 = module_0.NodeDLL(none_type_0)
    var_0 = node_d_l_l_0.__repr__()
    assert var_0 == 'Value: None'
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_14():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.size()
    assert var_1 == 1
    var_2 = bst_0.delete(bst_0)
    assert bst_0.root is None

def test_case_15():
    node_d_l_l_0 = module_0.NodeDLL()
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    queue_0 = module_0.Queue(node_d_l_l_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.dequeue()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert var_0.data is None
    assert var_0.next is None
    assert var_0.prev is None
    var_1 = node_d_l_l_0.__repr__()
    assert var_1 == 'Value: None'
    var_2 = bst_0.balance()
    assert var_2 == 0

def test_case_16():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.size()
    assert var_1 == 1
    var_2 = bst_0.delete(bst_0)
    assert bst_0.root is None

def test_case_17():
    float_0 = 418.0
    node_d_l_l_0 = module_0.NodeDLL()
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    queue_0 = module_0.Queue(node_d_l_l_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.dequeue()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert var_0.data is None
    assert var_0.next is None
    assert var_0.prev is None
    var_1 = bst_0.insert(var_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_2 = node_d_l_l_0.__repr__()
    assert var_2 == 'Value: None'
    var_3 = bst_0.balance()
    assert var_3 == 0

def test_case_18():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.contains(bst_0)
    assert var_0 is False
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_1 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_2 = bst_0.pre_order(bst_0)

def test_case_19():
    bool_0 = True
    bytes_0 = b'M\xb2tY\xcc\xc6\x84\xd7,Eo\xdb\xef\xd4\xf4'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.delete(bool_0)
    bst_1 = module_0.Bst()
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_1.root is None
    bool_1 = False
    var_1 = bst_1.search(bool_1)
    var_2 = bst_1.insert(bst_1)
    var_3 = bst_1.breadth_first()
    bst_2 = module_0.Bst(var_3)
    assert f'{type(bst_2).__module__}.{type(bst_2).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_2.root).__module__}.{type(bst_2.root).__qualname__}' == 'binarySearchTree3.Node'

def test_case_20():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.contains(bst_0)
    assert var_0 is False
    bool_0 = False
    var_1 = bst_0.search(bool_0)
    var_2 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_3 = bst_0.breadth_first()
    bst_1 = module_0.Bst(var_3)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'binarySearchTree3.Node'

def test_case_21():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.contains(bst_0)
    assert var_0 is False
    bool_0 = True
    var_1 = bst_0.contains(bool_0)
    var_2 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_3 = bst_0.post_order()
    bst_1 = module_0.Bst(var_3)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'binarySearchTree3.Node'
    var_4 = bst_1.contains(bst_0)
    assert var_4 is True

def test_case_22():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.contains(bst_0)
    assert var_0 is False
    bool_0 = True
    var_1 = bst_0.contains(bool_0)
    var_2 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_3 = bst_0.post_order()
    bst_1 = module_0.Bst(var_3)
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'binarySearchTree3.Node'
    var_4 = bst_1.contains(bst_0)
    assert var_4 is True

def test_case_23():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    queue_1 = module_0.Queue()
    var_0 = queue_1.size()
    assert var_0 == 0

def test_case_24():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None

def test_case_25():
    node_0 = module_0.Node()
    assert node_0.height == 1
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.in_order()
