#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree3/MIO/test_binarySearchTree3.py.orig
import pytest
import binarySearchTree3 as module_0

def test_case_0():
    bytes_0 = b'E\x9c\xce\xc8G'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'

def test_case_1():
    node_0 = module_0.Node()
    assert node_0.height == 1
    double_linked_list_0 = module_0.DoubleLinkedList(node_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'

def test_case_2():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_3():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.pre_order(bst_0)

def test_case_4():
    str_0 = 'aX}B^sw\x0cA!<Uq;!!D9'
    queue_0 = module_0.Queue(str_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.dequeue()
    assert var_0 == '9'

def test_case_5():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    queue_0 = module_0.Queue(bst_0)
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.dequeue()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert var_0.root is None

def test_case_6():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_7():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.enqueue(queue_0)

def test_case_8():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.append(double_linked_list_0)

def test_case_9():
    bytes_0 = b'@\x95\xef|X\x9c\x0b\xbd\x9d\xbd\x9d)\x19\xa9'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_0 = double_linked_list_0.shift()
    assert var_0 == 64

def test_case_10():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    double_linked_list_0 = module_0.DoubleLinkedList(bst_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_0 = double_linked_list_0.shift()
    assert double_linked_list_0.tail is None
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert var_0.root is None

def test_case_11():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(IndexError):
        double_linked_list_0.shift()

def test_case_12():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.remove(double_linked_list_0)
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_13():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.append(double_linked_list_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.append(var_0)
    var_2 = double_linked_list_0.remove(double_linked_list_0)

def test_case_14():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.push(var_0)
    var_2 = double_linked_list_0.remove(double_linked_list_0)

def test_case_15():
    bytes_0 = b'P\xa1\nA\xd6\xa0\xe5\xb0'
    double_linked_list_0 = module_0.DoubleLinkedList(bytes_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(bytes_0)

def test_case_16():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    var_0 = double_linked_list_0.push(double_linked_list_0)
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'
    with pytest.raises(ValueError):
        double_linked_list_0.remove(var_0)

def test_case_17():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    str_0 = '[][7i\x0bC@!8$I0g-L:21\x0c'
    var_0 = double_linked_list_0.append(str_0)
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    var_1 = double_linked_list_0.push(double_linked_list_0)
    var_2 = double_linked_list_0.push(var_1)
    var_3 = double_linked_list_0.remove(double_linked_list_0)

def test_case_18():
    double_linked_list_0 = module_0.DoubleLinkedList()
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None
    with pytest.raises(ValueError):
        double_linked_list_0.remove(double_linked_list_0)

def test_case_19():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.peek()

def test_case_20():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.delete(bst_0)
    assert bst_0.root is None

def test_case_21():
    bytes_0 = b'z\xc7'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'

def test_case_22():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_23():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None

def test_case_24():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'

def test_case_25():
    bytes_0 = b'd~\xd8\xfc\xfd,@,$\xb91f\xe7\x92\xc2\x14\xd3H'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'

def test_case_26():
    bytes_0 = b'\xeeq[\x16\xf3u\x82Q\x90\x1d\x1fj\xff1'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'

def test_case_27():
    str_0 = '_N*mxW@Y-+\x0c9z|?='
    bst_0 = module_0.Bst(str_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.delete(str_0)

def test_case_28():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'

def test_case_29():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.contains(bst_0)
    assert var_0 is False

def test_case_30():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.depth()
    assert var_1 == 1

def test_case_31():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.depth()
    assert var_0 == 0

def test_case_32():
    bytes_0 = b'j\xc4u.d\x0btT\x1f\xc1"\x0c.w\x85'
    bst_0 = module_0.Bst(bytes_0)
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_0 = bst_0.balance()
    assert var_0 == -1

def test_case_33():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_1 = bst_0.balance()
    assert var_1 == 0

def test_case_34():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.balance()
    assert var_0 == 0

def test_case_35():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None

def test_case_36():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.pre_order()
    double_linked_list_0 = module_0.DoubleLinkedList(var_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_37():
    node_d_l_l_0 = module_0.NodeDLL()
    list_0 = [node_d_l_l_0, node_d_l_l_0, node_d_l_l_0, node_d_l_l_0]
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.contains(node_d_l_l_0)
    assert var_0 is False
    var_1 = bst_0.in_order(list_0)

def test_case_38():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.in_order()
    double_linked_list_0 = module_0.DoubleLinkedList(var_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_39():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.post_order()
    var_1 = bst_0.size()
    assert var_1 == 0
    var_2 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    double_linked_list_0 = module_0.DoubleLinkedList(var_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'

def test_case_40():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.post_order()
    double_linked_list_0 = module_0.DoubleLinkedList(var_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_41():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.delete(bst_0)
    var_1 = bst_0.insert(var_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree3.Node'
    var_2 = bst_0.breadth_first()
    double_linked_list_0 = module_0.DoubleLinkedList(var_2)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert f'{type(double_linked_list_0.head).__module__}.{type(double_linked_list_0.head).__qualname__}' == 'binarySearchTree3.NodeDLL'
    assert f'{type(double_linked_list_0.tail).__module__}.{type(double_linked_list_0.tail).__qualname__}' == 'binarySearchTree3.NodeDLL'

def test_case_42():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.breadth_first()
    double_linked_list_0 = module_0.DoubleLinkedList(var_0)
    assert f'{type(double_linked_list_0).__module__}.{type(double_linked_list_0).__qualname__}' == 'binarySearchTree3.DoubleLinkedList'
    assert double_linked_list_0.head is None
    assert double_linked_list_0.tail is None

def test_case_43():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.delete(bst_0)

def test_case_44():
    node_d_l_l_0 = module_0.NodeDLL()

def test_case_45():
    node_d_l_l_0 = module_0.NodeDLL()
    var_0 = node_d_l_l_0.__repr__()
    assert var_0 == 'Value: None'

def test_case_46():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'

def test_case_47():
    queue_0 = module_0.Queue()
    assert f'{type(queue_0).__module__}.{type(queue_0).__qualname__}' == 'binarySearchTree3.Queue'
    var_0 = queue_0.size()
    assert var_0 == 0

def test_case_48():
    node_0 = module_0.Node()
    assert node_0.height == 1

def test_case_49():
    bst_0 = module_0.Bst()
    assert f'{type(bst_0).__module__}.{type(bst_0).__qualname__}' == 'binarySearchTree3.Bst'
    assert bst_0.root is None
    var_0 = bst_0.size()
    assert var_0 == 0
