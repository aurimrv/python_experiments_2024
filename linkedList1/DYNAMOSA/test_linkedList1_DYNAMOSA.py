#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList1/DYNAMOSA/test_linkedList1.py.orig
import pytest
import linkedList1 as module_0
import builtins as module_1

def test_case_0():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0

def test_case_1():
    float_0 = 1673.4114
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.__contains__(float_0)

def test_case_2():
    int_0 = -1461
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_0.__getitem__(int_0)

def test_case_3():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(StopIteration):
        doubly_linked_list_0.next()

def test_case_4():
    float_0 = 1673.4114
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 1
    var_1 = singly_linked_list_0.next()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList1.SinglyLinkedList'
    assert len(var_1) == 1
    singly_linked_list_1 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_1) == 0
    var_2 = singly_linked_list_1.__contains__(float_0)

def test_case_5():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.__contains__(doubly_linked_list_0)
    assert var_1 is True

def test_case_6():
    none_type_0 = None
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__len__()
    assert var_0 == 0
    var_1 = doubly_linked_list_0.append(none_type_0)
    assert len(doubly_linked_list_0) == 1

def test_case_7():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.__iter__()
    assert len(var_1) == 1
    var_2 = var_1.__contains__(var_1)
    assert var_2 is True

def test_case_8():
    int_0 = -2323
    singly_linked_node_0 = module_0.SinglyLinkedNode(int_0)
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0

def test_case_9():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.__contains__(singly_linked_list_0)
    var_1 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 1
    var_2 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 2
    var_3 = singly_linked_list_0.__iter__()
    assert len(var_3) == 2
    var_4 = singly_linked_list_0.append(var_2)
    assert len(singly_linked_list_0) == 3
    assert len(var_3) == 3
    var_5 = var_3.__setitem__(var_0, var_4)

def test_case_10():
    bool_0 = True
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(bool_0)
    assert len(doubly_linked_list_0) == 1
    with pytest.raises(StopIteration):
        doubly_linked_list_0.previous()

def test_case_11():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__iter__()
    assert len(var_0) == 0
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    var_1 = doubly_linked_list_1.__contains__(doubly_linked_list_1)
    assert var_1 is False
    doubly_linked_list_2 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_2) == 0
    doubly_linked_list_3 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_3) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_3.__getitem__(var_1)

def test_case_12():
    float_0 = 1672.3461366306228
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__contains__(float_0)
    assert var_0 is False
    doubly_linked_node_0 = module_0.DoublyLinkedNode(doubly_linked_list_0)
    assert f'{type(doubly_linked_node_0.data).__module__}.{type(doubly_linked_node_0.data).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(doubly_linked_node_0.data) == 0
    assert doubly_linked_node_0.next is None
    assert doubly_linked_node_0.prev is None
    var_1 = doubly_linked_list_0.append(float_0)
    assert len(doubly_linked_list_0) == 1
    assert len(doubly_linked_node_0.data) == 1
    with pytest.raises(IndexError):
        doubly_linked_list_0.insert(float_0, float_0)

def test_case_13():
    bytes_0 = b'}\xd9\xff\xe7\xea\xfbPJk\x0328\x8b\xd4`'
    bool_0 = False
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(bool_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.__contains__(bytes_0)
    assert var_1 is False
    object_0 = module_1.object()
    var_2 = doubly_linked_list_0.append(object_0)
    assert len(doubly_linked_list_0) == 2
    var_3 = module_0.DoublyLinkedNode(var_2)
    assert var_3.prev is None

def test_case_14():
    bool_0 = False
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_0.__setitem__(bool_0, doubly_linked_list_0)

def test_case_15():
    float_0 = 1672.3461366306228
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(float_0)
    assert len(doubly_linked_list_0) == 1
    doubly_linked_node_0 = module_0.DoublyLinkedNode(doubly_linked_list_0)
    assert f'{type(doubly_linked_node_0.data).__module__}.{type(doubly_linked_node_0.data).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(doubly_linked_node_0.data) == 1
    assert doubly_linked_node_0.next is None
    assert doubly_linked_node_0.prev is None
    var_1 = doubly_linked_list_0.append(float_0)
    assert len(doubly_linked_list_0) == 2
    assert len(doubly_linked_node_0.data) == 2
    with pytest.raises(IndexError):
        doubly_linked_list_0.insert(float_0, float_0)

def test_case_16():
    bytes_0 = b'}\xd9\xff\xe7\xea\xfbPJk\x0328\x8b\xd4`'
    bool_0 = False
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(bool_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.__contains__(bytes_0)
    assert var_1 is False
    object_0 = module_1.object()
    var_2 = doubly_linked_list_0.append(object_0)
    assert len(doubly_linked_list_0) == 2
    var_3 = doubly_linked_list_0.__iter__()
    assert len(var_3) == 2
    var_4 = var_3.__contains__(object_0)
    assert var_4 is True
    var_5 = var_3.__setitem__(bool_0, var_2)
    var_6 = var_3.__contains__(doubly_linked_list_0)
    assert var_6 is False

def test_case_17():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__contains__(doubly_linked_list_0)
    assert var_0 is False
    object_0 = module_1.object()
    var_1 = doubly_linked_list_0.append(object_0)
    assert len(doubly_linked_list_0) == 1
    var_2 = doubly_linked_list_0.__setitem__(var_0, var_1)
    var_3 = doubly_linked_list_0.insert(var_2, var_0)
    assert len(doubly_linked_list_0) == 3

def test_case_18():
    bool_0 = False
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(bool_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.next()
    assert var_1 is False
    var_2 = doubly_linked_list_0.__contains__(var_0)
    assert var_2 is False
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_3 = doubly_linked_list_0.append(singly_linked_list_0)
    assert len(doubly_linked_list_0) == 2
    var_4 = doubly_linked_list_0.__iter__()
    assert len(var_4) == 2
    var_5 = var_4.__setitem__(bool_0, var_3)
    var_6 = doubly_linked_list_0.insert(var_4, var_2)
    assert len(doubly_linked_list_0) == 3
    assert len(var_4) == 3

def test_case_19():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    bytes_0 = b'}\xd9\xff\xe7\xea\xfbPJk\x0328\x8b\xd4`'
    bool_0 = False
    var_0 = doubly_linked_list_0.__iter__()
    assert len(var_0) == 0
    var_1 = var_0.append(bool_0)
    assert len(doubly_linked_list_0) == 1
    assert len(var_0) == 1
    var_2 = var_0.__contains__(bytes_0)
    assert var_2 is False
    object_0 = module_1.object()
    var_3 = var_0.append(object_0)
    assert len(doubly_linked_list_0) == 2
    assert len(var_0) == 2
    var_4 = var_0.__iter__()
    assert len(var_4) == 2
    var_5 = var_0.append(bytes_0)
    assert len(doubly_linked_list_0) == 3
    assert len(var_0) == 3
    assert len(var_4) == 3
    var_6 = var_4.__setitem__(bool_0, var_3)
    with pytest.raises(StopIteration):
        var_0.previous()

def test_case_20():
    bool_0 = True
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(bool_0)
    assert len(doubly_linked_list_0) == 1
    none_type_0 = None
    var_1 = doubly_linked_list_0.__contains__(none_type_0)
    assert var_1 is False
    object_0 = module_1.object()
    var_2 = doubly_linked_list_0.append(object_0)
    assert len(doubly_linked_list_0) == 2
    var_3 = doubly_linked_list_0.__iter__()
    assert len(var_3) == 2
    var_4 = var_3.__contains__(object_0)
    assert var_4 is True
    var_5 = var_3.__setitem__(bool_0, var_2)
    var_6 = var_3.__contains__(doubly_linked_list_0)
    assert var_6 is False
    with pytest.raises(StopIteration):
        doubly_linked_list_0.previous()

def test_case_21():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    bool_0 = True
    var_0 = doubly_linked_list_0.__iter__()
    assert len(var_0) == 0
    var_1 = var_0.append(bool_0)
    assert len(doubly_linked_list_0) == 1
    assert len(var_0) == 1
    var_2 = var_0.__iter__()
    assert len(var_2) == 1
    var_3 = var_0.append(var_1)
    assert len(doubly_linked_list_0) == 2
    assert len(var_0) == 2
    assert len(var_2) == 2
    singly_linked_list_0 = var_0.append(var_3)
    assert len(doubly_linked_list_0) == 3
    assert len(var_0) == 3
    assert len(var_2) == 3
    var_4 = var_0.next()
    assert var_4 is True
    var_5 = var_0.__contains__(var_4)
    assert var_5 is True
    object_0 = module_1.object()
    var_6 = var_0.append(object_0)
    assert len(doubly_linked_list_0) == 4
    assert len(var_0) == 4
    assert len(var_2) == 4
    var_7 = var_0.__iter__()
    assert len(var_7) == 4
    var_8 = var_7.__setitem__(bool_0, var_6)
    var_9 = var_7.__contains__(var_0)
    assert var_9 is False
    var_10 = var_0.insert(var_7, var_5)
    assert len(doubly_linked_list_0) == 5
    assert len(var_0) == 5
    assert len(var_2) == 5
    assert len(var_7) == 5

def test_case_22():
    bytes_0 = b'}\xd9\xff\xe7\xea\xfbPJk\x0328\x8b\xd4`'
    bool_0 = False
    singly_linked_node_0 = module_0.SinglyLinkedNode(bool_0)
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(bool_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.__contains__(bytes_0)
    assert var_1 is False
    var_2 = doubly_linked_list_0.insert(bytes_0, bool_0)
    assert len(doubly_linked_list_0) == 3
    object_0 = module_1.object()
    var_3 = doubly_linked_list_0.append(object_0)
    assert len(doubly_linked_list_0) == 4
    var_4 = doubly_linked_list_0.__iter__()
    assert len(var_4) == 4
    var_5 = var_4.__contains__(object_0)
    assert var_5 is True
    var_6 = var_4.__setitem__(bool_0, var_3)
    var_7 = var_4.__getitem__(var_5)
    assert var_7 == b'}\xd9\xff\xe7\xea\xfbPJk\x0328\x8b\xd4`'
    with pytest.raises(StopIteration):
        var_4.previous()

def test_case_23():
    bytes_0 = b'}\xd9\xff\xe7\xea\xfbPJk\x0328\x8b\xd4`'
    bool_0 = False
    singly_linked_node_0 = module_0.SinglyLinkedNode(bool_0)
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(bool_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.__contains__(bytes_0)
    assert var_1 is False
    var_2 = doubly_linked_list_0.insert(bytes_0, bool_0)
    assert len(doubly_linked_list_0) == 3
    object_0 = module_1.object()
    var_3 = doubly_linked_list_0.append(object_0)
    assert len(doubly_linked_list_0) == 4
    var_4 = doubly_linked_list_0.__iter__()
    assert len(var_4) == 4
    var_5 = var_4.__contains__(object_0)
    assert var_5 is True
    var_6 = doubly_linked_list_0.next()
    assert var_6 is False
    var_7 = var_4.previous()
    assert var_7 is False
    var_8 = var_4.__contains__(doubly_linked_list_0)
    assert var_8 is False
    with pytest.raises(StopIteration):
        doubly_linked_list_0.previous()

def test_case_24():
    int_0 = -588
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_0.__setitem__(int_0, int_0)

def test_case_25():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__iter__()
    assert len(var_0) == 0
    var_1 = var_0.append(var_0)
    assert len(doubly_linked_list_0) == 1
    assert len(var_0) == 1
    var_2 = var_0.append(var_1)
    assert len(doubly_linked_list_0) == 2
    assert len(var_0) == 2
    var_3 = var_0.__contains__(var_1)
    assert var_3 is True
    var_4 = var_0.append(var_3)
    assert len(doubly_linked_list_0) == 3
    assert len(var_0) == 3
    var_5 = var_0.__iter__()
    assert len(var_5) == 3
    var_6 = var_5.__setitem__(var_3, var_4)
    var_7 = var_5.__contains__(var_0)
    assert var_7 is True
    var_8 = var_0.insert(var_5, var_3)
    assert len(doubly_linked_list_0) == 4
    assert len(var_0) == 4
    assert len(var_5) == 4

def test_case_26():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    bool_0 = True
    var_0 = doubly_linked_list_0.__iter__()
    assert len(var_0) == 0
    var_1 = var_0.append(bool_0)
    assert len(doubly_linked_list_0) == 1
    assert len(var_0) == 1
    var_2 = doubly_linked_list_0.__len__()
    assert var_2 == 1
    var_3 = var_0.append(var_1)
    assert len(doubly_linked_list_0) == 2
    assert len(var_0) == 2
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_4 = module_0.DoublyLinkedList()
    assert len(var_4) == 0
    var_5 = var_0.__contains__(var_1)
    assert var_5 is True
    var_6 = var_0.append(var_2)
    assert len(doubly_linked_list_0) == 3
    assert len(var_0) == 3
    var_7 = var_0.append(var_6)
    assert len(doubly_linked_list_0) == 4
    assert len(var_0) == 4
    doubly_linked_node_0 = module_0.DoublyLinkedNode(singly_linked_list_0)
    assert len(doubly_linked_node_0.data) == 0
    assert doubly_linked_node_0.prev is None
    var_8 = singly_linked_list_0.append(var_4)
    assert len(singly_linked_list_0) == 1
    assert len(doubly_linked_node_0.data) == 1
    var_9 = var_0.__iter__()
    assert len(var_9) == 4
    var_10 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 2
    assert len(doubly_linked_node_0.data) == 2
    var_11 = var_9.__setitem__(bool_0, var_7)
    var_12 = singly_linked_list_0.append(var_11)
    assert len(singly_linked_list_0) == 3
    assert len(doubly_linked_node_0.data) == 3
    var_13 = var_0.insert(var_9, var_5)
    assert len(doubly_linked_list_0) == 5
    assert len(var_0) == 5
    assert len(var_9) == 5
    var_14 = singly_linked_list_0.append(var_13)
    assert len(singly_linked_list_0) == 4
    assert len(doubly_linked_node_0.data) == 4

def test_case_27():
    int_0 = -1313
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.insert(int_0, int_0)
    assert len(doubly_linked_list_0) == 1

def test_case_28():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    bool_0 = True
    var_0 = doubly_linked_list_0.__iter__()
    assert len(var_0) == 0
    var_1 = var_0.append(bool_0)
    assert len(doubly_linked_list_0) == 1
    assert len(var_0) == 1
    var_2 = doubly_linked_list_0.__len__()
    assert var_2 == 1
    var_3 = var_0.append(var_1)
    assert len(doubly_linked_list_0) == 2
    assert len(var_0) == 2
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_4 = var_0.next()
    assert var_4 is True
    var_5 = doubly_linked_list_0.__len__()
    assert var_5 == 2
    var_6 = var_0.append(var_2)
    assert len(doubly_linked_list_0) == 3
    assert len(var_0) == 3
    var_7 = var_0.append(var_6)
    assert len(doubly_linked_list_0) == 4
    assert len(var_0) == 4
    var_8 = singly_linked_list_0.append(var_4)
    assert len(singly_linked_list_0) == 1
    var_9 = singly_linked_list_0.__iter__()
    assert len(var_9) == 1
    var_10 = var_0.__iter__()
    assert len(var_10) == 4
    var_11 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 2
    assert len(var_9) == 2
    var_12 = var_10.__setitem__(bool_0, var_7)
    var_13 = var_10.__contains__(var_0)
    assert var_13 is False
    var_14 = var_0.insert(var_10, var_5)
    assert len(doubly_linked_list_0) == 5
    assert len(var_0) == 5
    assert len(var_10) == 5
    var_15 = singly_linked_list_0.append(var_14)
    assert len(singly_linked_list_0) == 3
    assert len(var_9) == 3
