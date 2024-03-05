#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList1/MOSA/test_linkedList1.py.orig
import pytest
import linkedList1 as module_0

def test_case_0():
    singly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(singly_linked_list_0) == 0

def test_case_1():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = singly_linked_list_0.__contains__(doubly_linked_list_0)
    var_1 = singly_linked_list_0.__len__()
    assert var_1 == 0
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    var_2 = doubly_linked_list_1.append(doubly_linked_list_1)
    assert len(doubly_linked_list_1) == 1
    var_3 = doubly_linked_list_1.__contains__(doubly_linked_list_1)
    assert var_3 is True
    var_4 = singly_linked_list_0.append(doubly_linked_list_1)
    assert len(singly_linked_list_0) == 1

def test_case_2():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    singly_linked_list_1 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_1) == 0
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    var_0 = doubly_linked_list_1.append(doubly_linked_list_1)
    assert len(doubly_linked_list_1) == 1
    int_0 = -2493
    with pytest.raises(IndexError):
        singly_linked_list_1.__getitem__(int_0)

def test_case_3():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(StopIteration):
        doubly_linked_list_0.next()

def test_case_4():
    float_0 = 4134.0
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.append(float_0)
    assert len(singly_linked_list_0) == 1

def test_case_5():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.__contains__(doubly_linked_list_0)
    assert var_1 is True

def test_case_6():
    singly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(singly_linked_list_0) == 0
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = singly_linked_list_0.__len__()
    assert var_0 == 0
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    var_1 = doubly_linked_list_1.append(doubly_linked_list_1)
    assert len(doubly_linked_list_1) == 1
    var_2 = doubly_linked_list_1.__contains__(doubly_linked_list_1)
    assert var_2 is True

def test_case_7():
    int_0 = -460
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__iter__()
    assert len(var_0) == 0
    var_1 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    assert len(var_0) == 1

def test_case_8():
    int_0 = -2323
    singly_linked_node_0 = module_0.SinglyLinkedNode(int_0)
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0

def test_case_9():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.__iter__()
    assert len(var_1) == 1
    var_2 = var_1.__contains__(var_0)
    assert var_2 is False
    var_3 = var_1.next()
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(var_3) == 1
    var_4 = var_1.insert(var_3, var_2)
    assert len(doubly_linked_list_0) == 3
    assert len(var_1) == 3
    assert len(var_3) == 3
    var_5 = doubly_linked_list_0.__len__()
    assert var_5 == 3

def test_case_10():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__len__()
    assert var_0 == 0
    var_1 = doubly_linked_list_0.append(var_0)
    assert len(doubly_linked_list_0) == 1
    var_2 = doubly_linked_list_0.__iter__()
    assert len(var_2) == 1
    var_3 = var_2.append(var_2)
    assert len(doubly_linked_list_0) == 2
    assert len(var_2) == 2
    var_4 = var_2.__contains__(var_0)
    assert var_4 is True
    var_5 = var_2.insert(var_2, var_4)
    assert len(doubly_linked_list_0) == 4
    assert len(var_2) == 4
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_6 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 1
    var_7 = singly_linked_list_0.append(var_4)
    assert len(singly_linked_list_0) == 2
    var_8 = singly_linked_list_0.append(var_7)
    assert len(singly_linked_list_0) == 3
    with pytest.raises(StopIteration):
        var_2.previous()

def test_case_11():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = singly_linked_list_0.__len__()
    assert var_0 == 0
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    var_1 = doubly_linked_list_1.append(doubly_linked_list_1)
    assert len(doubly_linked_list_1) == 1
    var_2 = doubly_linked_list_1.append(doubly_linked_list_0)
    assert len(doubly_linked_list_1) == 2

def test_case_12():
    int_0 = -483
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.insert(int_0, int_0)
    assert len(doubly_linked_list_0) == 1
    singly_linked_list_0 = doubly_linked_list_0.__contains__(var_0)
    assert singly_linked_list_0 is False

def test_case_13():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = singly_linked_list_0.__contains__(doubly_linked_list_0)
    singly_linked_list_1 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_1) == 0
    var_1 = singly_linked_list_0.__len__()
    assert var_1 == 0
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    var_2 = doubly_linked_list_1.append(doubly_linked_list_1)
    assert len(doubly_linked_list_1) == 1
    var_3 = doubly_linked_list_1.__contains__(doubly_linked_list_1)
    assert var_3 is True
    with pytest.raises(IndexError):
        singly_linked_list_0.__getitem__(var_3)

def test_case_14():
    bool_0 = True
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    with pytest.raises(IndexError):
        singly_linked_list_0.__setitem__(bool_0, bool_0)

def test_case_15():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__contains__(doubly_linked_list_0)
    assert var_0 is False
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    var_1 = doubly_linked_list_1.__len__()
    assert var_1 == 0
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_2 = singly_linked_list_0.append(doubly_linked_list_1)
    assert len(singly_linked_list_0) == 1
    var_3 = singly_linked_list_0.__getitem__(var_0)
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(var_3) == 0

def test_case_16():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = singly_linked_list_0.__contains__(doubly_linked_list_0)
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    var_1 = doubly_linked_list_1.append(doubly_linked_list_1)
    assert len(doubly_linked_list_1) == 1
    singly_linked_node_0 = module_0.SinglyLinkedNode(doubly_linked_list_0)
    assert len(singly_linked_node_0.data) == 0
    var_2 = doubly_linked_list_1.__setitem__(var_0, doubly_linked_list_0)

def test_case_17():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    var_0 = doubly_linked_list_1.__contains__(doubly_linked_list_0)
    assert var_0 is False
    var_1 = doubly_linked_list_1.__len__()
    assert var_1 == 0
    doubly_linked_list_2 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_2) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_1.insert(doubly_linked_list_2, var_0)

def test_case_18():
    int_0 = -460
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1

def test_case_19():
    float_0 = 4134.0
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.append(float_0)
    assert len(singly_linked_list_0) == 1
    var_1 = singly_linked_list_0.append(float_0)
    assert len(singly_linked_list_0) == 2

def test_case_20():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__len__()
    assert var_0 == 0
    var_1 = doubly_linked_list_0.append(var_0)
    assert len(doubly_linked_list_0) == 1
    var_2 = doubly_linked_list_0.__iter__()
    assert len(var_2) == 1
    var_3 = var_2.append(var_2)
    assert len(doubly_linked_list_0) == 2
    assert len(var_2) == 2
    var_4 = var_2.__contains__(doubly_linked_list_0)
    assert var_4 is True
    var_5 = var_2.insert(var_2, var_4)
    assert len(doubly_linked_list_0) == 4
    assert len(var_2) == 4
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_6 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 1
    str_0 = '{sQ*%g\t>14:@;'
    singly_linked_node_0 = module_0.SinglyLinkedNode(str_0)
    var_7 = singly_linked_list_0.append(var_4)
    assert len(singly_linked_list_0) == 2
    var_8 = singly_linked_list_0.append(var_7)
    assert len(singly_linked_list_0) == 3
    with pytest.raises(StopIteration):
        var_2.previous()

def test_case_21():
    int_0 = -483
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.insert(int_0, int_0)
    assert len(doubly_linked_list_0) == 1

def test_case_22():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__len__()
    assert var_0 == 0
    var_1 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_2 = doubly_linked_list_0.append(var_1)
    assert len(doubly_linked_list_0) == 2
    var_3 = doubly_linked_list_0.__iter__()
    assert len(var_3) == 2
    var_4 = var_3.append(var_3)
    assert len(doubly_linked_list_0) == 3
    assert len(var_3) == 3
    var_5 = var_3.insert(var_3, var_0)
    assert len(doubly_linked_list_0) == 4
    assert len(var_3) == 4
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_6 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 1
    str_0 = '{sQ*%g\t>14:@;'
    singly_linked_node_0 = module_0.SinglyLinkedNode(str_0)
    var_7 = singly_linked_list_0.append(var_3)
    assert len(singly_linked_list_0) == 2
    var_8 = singly_linked_list_0.append(var_7)
    assert len(singly_linked_list_0) == 3
    with pytest.raises(StopIteration):
        var_3.previous()

def test_case_23():
    float_0 = -2002.959
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    with pytest.raises(IndexError):
        singly_linked_list_0.__setitem__(float_0, float_0)

def test_case_24():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.__iter__()
    assert len(var_1) == 1
    var_2 = var_1.__contains__(var_0)
    assert var_2 is False
    var_3 = var_1.next()
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(var_3) == 1
    var_4 = var_1.insert(var_3, var_2)
    assert len(doubly_linked_list_0) == 3
    assert len(var_1) == 3
    assert len(var_3) == 3
    var_5 = var_3.__len__()
    assert var_5 == 3
    var_6 = doubly_linked_list_0.append(var_2)
    assert len(doubly_linked_list_0) == 4
    assert len(var_1) == 4
    assert len(var_3) == 4
    var_7 = var_1.__contains__(var_0)
    var_8 = var_1.append(var_2)
    assert len(doubly_linked_list_0) == 5
    assert len(var_1) == 5
    assert len(var_3) == 5
    var_9 = doubly_linked_list_0.__contains__(var_2)
    assert var_9 is True

def test_case_25():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.append(var_0)
    assert len(doubly_linked_list_0) == 2
    var_2 = doubly_linked_list_0.__iter__()
    assert len(var_2) == 2
    var_3 = var_2.__contains__(var_0)
    assert var_3 is True
    var_4 = var_2.next()
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(var_4) == 2
    var_5 = doubly_linked_list_0.__getitem__(var_3)
    var_6 = var_2.insert(var_4, var_3)
    assert len(doubly_linked_list_0) == 4
    assert len(var_2) == 4
    assert len(var_4) == 4
    var_7 = var_4.__len__()
    assert var_7 == 4
    var_8 = var_2.__contains__(var_0)
    assert var_8 is True
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0

def test_case_26():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.append(var_0)
    assert len(doubly_linked_list_0) == 2
    var_2 = doubly_linked_list_0.__iter__()
    assert len(var_2) == 2
    var_3 = var_2.append(var_2)
    assert len(doubly_linked_list_0) == 3
    assert len(var_2) == 3
    var_4 = var_2.__contains__(var_0)
    assert var_4 is True
    var_5 = doubly_linked_list_0.__setitem__(var_4, var_4)
    var_6 = var_2.insert(var_2, var_4)
    assert len(doubly_linked_list_0) == 4
    assert len(var_2) == 4

def test_case_27():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.append(var_0)
    assert len(doubly_linked_list_0) == 2
    var_2 = doubly_linked_list_0.__iter__()
    assert len(var_2) == 2
    var_3 = var_2.append(var_2)
    assert len(doubly_linked_list_0) == 3
    assert len(var_2) == 3
    var_4 = var_2.__contains__(var_0)
    assert var_4 is True
    var_5 = var_2.next()
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(var_5) == 3
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_6 = singly_linked_list_0.append(var_4)
    assert len(singly_linked_list_0) == 1
    var_7 = var_2.previous()
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(var_7) == 3
    bytes_0 = b'\xa7'

def test_case_28():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__len__()
    assert var_0 == 0
    var_1 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_2 = doubly_linked_list_0.append(var_1)
    assert len(doubly_linked_list_0) == 2
    var_3 = doubly_linked_list_0.__iter__()
    assert len(var_3) == 2
    var_4 = var_3.append(var_3)
    assert len(doubly_linked_list_0) == 3
    assert len(var_3) == 3
    var_5 = var_3.__contains__(var_1)
    assert var_5 is True
    var_6 = var_3.insert(var_3, var_5)
    assert len(doubly_linked_list_0) == 4
    assert len(var_3) == 4
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_7 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 1
    str_0 = '{sQ*%g\t>14:@;'
    singly_linked_node_0 = module_0.SinglyLinkedNode(str_0)
    var_8 = singly_linked_list_0.append(var_5)
    assert len(singly_linked_list_0) == 2
    var_9 = singly_linked_list_0.append(var_8)
    assert len(singly_linked_list_0) == 3
    var_10 = singly_linked_list_0.append(var_5)
    assert len(singly_linked_list_0) == 4
