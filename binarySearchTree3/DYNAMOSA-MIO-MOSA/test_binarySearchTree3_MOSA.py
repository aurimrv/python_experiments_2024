#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree3/MOSA/test_binarySearchTree3.py.orig
import pytest
import binarySearchTree3 as module_0

def test_case_0():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.breadth_first()
    var_1 = bst_0.size()
    assert var_1 == 0
    var_2 = bst_0.insert(var_1)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    double_linked_list_0 = module_0.DoubleLinkedList(var_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'

def test_case_1():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    double_linked_list_1 = module_0.DoubleLinkedList(double_linked_list_0)
    assert f'{type(double_linked_list_1).__module__}.{type(double_linked_list_1).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_1.head).__module__}.{type(double_linked_list_1.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_0 = double_linked_list_0.push(double_linked_list_1)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.append(var_0)
    var_2 = double_linked_list_0.remove(var_1)

def test_case_2():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_3():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    double_linked_list_1 = module_0.DoubleLinkedList(double_linked_list_0)
    assert f'{type(double_linked_list_1).__module__}.{type(double_linked_list_1).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_1.head).__module__}.{type(double_linked_list_1.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_0 = double_linked_list_0.push(double_linked_list_1)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.push(double_linked_list_0)
    var_2 = double_linked_list_0.remove(double_linked_list_0)

def test_case_4():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.append(var_0)
    var_2 = double_linked_list_0.remove(var_1)

def test_case_5():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(bst_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.push(double_linked_list_0)
    var_2 = bst_0.in_order(bst_0)
    var_3 = double_linked_list_0.pop()
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(var_3.head).__module__}.{type(var_3.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(var_3.tail).__module__}.{type(var_3.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_4 = bst_0.contains(var_2)
    assert var_4 is False
    var_5 = double_linked_list_0.shift()
    assert double_linked_list_0.tail is None
    assert var_3.tail is None
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'binarySearchTree3.Bst'
    assert var_5.root is None

def test_case_6():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.peek()

def test_case_7():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'

def test_case_8():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.depth()
    assert var_0 == 0
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_1 = double_linked_list_0.append(bst_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_2 = double_linked_list_0.push(double_linked_list_0)
    var_3 = double_linked_list_0.remove(double_linked_list_0)
    var_4 = bst_0.post_order(var_3)
    var_5 = bst_0.contains(double_linked_list_0)
    assert var_5 is False
    var_6 = bst_0.delete(bst_0)
    var_7 = double_linked_list_0.shift()
    assert double_linked_list_0.tail is None
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'binarySearchTree3.Bst'
    assert var_7.root is None

def test_case_9():
    bool_0 = True
    node_d_l_l_0 = module_0.NodeDLL(prev=bool_0)
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.shift()

def test_case_10():
    int_0 = 76
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(int_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.remove(int_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_11():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(ValueError):
        double_linked_list_0.remove(double_linked_list_0)

def test_case_12():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.peek()

def test_case_13():
    bytes_0 = b';9q\xd5\xe4\\!+v\xc3\xb2\x97\xf0'
    none_type_0 = None
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.balance()
    assert var_0 == -3

def test_case_14():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None

def test_case_15():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.delete(bst_0)
    assert bst_0.root is None

def test_case_16():
    bool_0 = False
    bytes_0 = b'\xa6"\x8b\xdam\xe3\x8fL\xeb\xcb\xeb\x95\xec'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.delete(bool_0)

def test_case_17():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.pre_order()
    queue_0 = module_0.Queue(var_1)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_18():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.search(bst_0)
    var_1 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_2 = bst_0.delete(bst_0)
    assert bst_0.root is None

def test_case_19():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    double_linked_list_0 = module_0.DoubleLinkedList(bst_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_0 = bst_0.depth()
    assert var_0 == 0

def test_case_20():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.post_order()
    queue_0 = module_0.Queue(var_1)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_2 = bst_0.balance()
    assert var_2 == 0
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_21():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.depth()
    assert var_0 == 0
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    double_linked_list_1 = module_0.DoubleLinkedList(double_linked_list_0)
    assert f'{type(double_linked_list_1).__module__}.{type(double_linked_list_1).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_1.head).__module__}.{type(double_linked_list_1.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.append(bst_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_2 = double_linked_list_0.push(double_linked_list_0)
    var_3 = double_linked_list_0.remove(double_linked_list_0)
    var_4 = bst_0.balance()
    assert var_4 == 0
    var_5 = bst_0.contains(double_linked_list_0)
    assert var_5 is False
    var_6 = bst_0.delete(bst_0)
    var_7 = double_linked_list_0.shift()
    assert double_linked_list_0.tail is None
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'binarySearchTree3.Bst'
    assert var_7.root is None

def test_case_22():
    bytes_0 = b'\xa6"\x8b\xdam\xe3\x8fL\xeb\xcb\xeb\x95\xec'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'

def test_case_23():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.delete(bst_0)
    var_1 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_2 = bst_0.delete(bst_0)
    assert bst_0.root is None

def test_case_24():
    node_d_l_l_0 = module_0.NodeDLL()

def test_case_25():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    node_d_l_l_0 = module_0.NodeDLL()
    var_0 = node_d_l_l_0.__repr__()
    assert var_0 == 'Value: None'
    var_1 = node_d_l_l_0.__repr__()
    assert var_1 == 'Value: None'

def test_case_26():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.size()
    assert var_0 == 0
    var_1 = bst_0.post_order()
    var_2 = bst_0.insert(var_1)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_3 = bst_0.delete(var_1)
    assert bst_0.root is None

def test_case_27():
    node_0 = module_0.Node()
    assert node_0.height == 1

def test_case_28():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.depth()
    assert var_0 == 0
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    double_linked_list_1 = var_0.__repr__()
    assert double_linked_list_1 == '0'
    var_1 = double_linked_list_0.push(double_linked_list_1)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_2 = double_linked_list_0.append(bst_0)
    var_3 = double_linked_list_0.push(double_linked_list_0)
    var_4 = double_linked_list_0.remove(double_linked_list_0)
    var_5 = bst_0.post_order(var_4)
    var_6 = bst_0.contains(double_linked_list_0)
    assert var_6 is False
    var_7 = bst_0.delete(bst_0)
    var_8 = double_linked_list_0.shift()
    assert f'{type(var_8).__module__}.{type(var_8).__qualname__}' == 'binarySearchTree3.Bst'
    assert var_8.root is None

def test_case_29():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.depth()
    assert var_0 == 0
    var_1 = bst_0.__repr__()
    var_2 = bst_0.delete(bst_0)
    var_3 = bst_0.in_order()
    double_linked_list_0 = module_0.DoubleLinkedList(var_3)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_4 = double_linked_list_0.push(var_2)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(var_3)

def test_case_30():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.delete(bst_0)
    var_1 = bst_0.breadth_first()
    var_2 = bst_0.size()
    assert var_2 == 0
    var_3 = bst_0.insert(var_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    double_linked_list_0 = module_0.DoubleLinkedList(var_1)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_4 = bst_0.depth()
    assert var_4 == 1

def test_case_31():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.delete(bst_0)
    var_1 = bst_0.in_order()
    var_2 = bst_0.breadth_first()
    double_linked_list_0 = module_0.DoubleLinkedList(var_2)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_32():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.depth()
    assert var_0 == 0
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    double_linked_list_1 = module_0.DoubleLinkedList(double_linked_list_0)
    assert f'{type(double_linked_list_1).__module__}.{type(double_linked_list_1).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_1.head).__module__}.{type(double_linked_list_1.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_1.tail).__module__}.{type(double_linked_list_1.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.push(bst_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    node_0 = module_0.Node()
    assert node_0.height == 1
    var_2 = double_linked_list_0.append(bst_0)
    var_3 = double_linked_list_0.push(double_linked_list_0)
    var_4 = double_linked_list_0.remove(bst_0)
    var_5 = bst_0.contains(double_linked_list_0)
    assert var_5 is False
    var_6 = bst_0.delete(bst_0)

def test_case_33():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.pre_order()
    queue_0 = module_0.Queue(var_1)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_34():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.depth()
    assert var_0 == 0
    double_linked_list_0 = bst_0.post_order(bst_0)

def test_case_35():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.in_order()
    queue_0 = module_0.Queue(var_1)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_2 = queue_0.peek()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(var_2.root).__module__}.{type(var_2.root).__qualname__}' == 'binarySearchTree3.Node'

def test_case_36():
    bool_0 = False
    bytes_0 = b'\xd0\xb8\x9b'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.in_order()
    var_1 = module_0.Bst()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'binarySearchTree3.Bst'
    assert var_1.root is None
    var_2 = bst_0.in_order()
    queue_0 = module_0.Queue(var_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_37():
    bool_0 = False
    bytes_0 = b'\xcb\xd9\xfd3fS\x94r<=\xbd\xad\x87'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.in_order()
    bst_1 = module_0.Bst()
    assert f'{type(bst_1).__module__}.{type(bst_1).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_1.root is None
    var_1 = bst_0.in_order()
    queue_0 = module_0.Queue(var_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_38():
    str_0 = 'XGqyAY`1?\n[fq%6QZ'
    bst_0 = module_0.Bst(str_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.delete(str_0)
