#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList1/MIO/test_linkedList1.py.orig
import pytest
import linkedList1 as module_0

def test_case_0():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0

def test_case_1():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.__contains__(doubly_linked_list_0)
    assert var_1 is True

def test_case_2():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.__contains__(var_0)
    assert var_1 is False

def test_case_3():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.append(var_0)
    assert len(doubly_linked_list_0) == 2
    var_2 = doubly_linked_list_0.__contains__(var_0)
    assert var_2 is True

def test_case_4():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__contains__(doubly_linked_list_0)
    assert var_0 is False

def test_case_5():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 1
    var_1 = singly_linked_list_0.next()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList1.SinglyLinkedList'
    assert len(var_1) == 1
    var_2 = var_1.__contains__(var_0)
    assert var_2 is False
    singly_linked_list_1 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_1) == 0
    var_3 = var_1.__iter__()
    assert len(var_3) == 1
    singly_linked_list_2 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_2) == 0
    bool_0 = True
    var_4 = var_3.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 2
    assert len(var_1) == 2
    assert len(var_3) == 2
    var_5 = singly_linked_list_0.__getitem__(bool_0)
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'linkedList1.SinglyLinkedList'
    assert len(var_5) == 2

def test_case_6():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__contains__(doubly_linked_list_0)
    assert var_0 is False
    var_1 = doubly_linked_list_0.append(var_0)
    assert len(doubly_linked_list_0) == 1
    var_2 = doubly_linked_list_0.__getitem__(var_0)
    assert var_2 is False

def test_case_7():
    float_0 = -2092.0
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_0.__getitem__(float_0)

def test_case_8():
    bool_0 = False
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_0.__getitem__(bool_0)

def test_case_9():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    bool_0 = False
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.__setitem__(bool_0, bool_0)

def test_case_10():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    int_0 = -641
    with pytest.raises(IndexError):
        doubly_linked_list_0.__setitem__(int_0, int_0)

def test_case_11():
    bool_0 = False
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_0.__setitem__(bool_0, bool_0)

def test_case_12():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(StopIteration):
        doubly_linked_list_0.next()

def test_case_13():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.next()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(var_1) == 1

def test_case_14():
    none_type_0 = None
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.append(none_type_0)
    assert len(singly_linked_list_0) == 1
    var_1 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 2
    var_2 = singly_linked_list_0.__contains__(none_type_0)
    assert var_2 is True
    var_3 = singly_linked_list_0.append(none_type_0)
    assert len(singly_linked_list_0) == 3

def test_case_15():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 1
    var_1 = singly_linked_list_0.__contains__(var_0)
    assert var_1 is False
    var_2 = singly_linked_list_0.append(var_1)
    assert len(singly_linked_list_0) == 2

def test_case_16():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 1
    singly_linked_list_1 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_1) == 0
    var_1 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 2
    var_2 = singly_linked_list_0.next()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList1.SinglyLinkedList'
    assert len(var_2) == 2
    var_3 = var_2.__contains__(singly_linked_list_1)
    assert var_3 is False
    singly_linked_list_2 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_2) == 0
    var_4 = var_2.__iter__()
    assert len(var_4) == 2
    singly_linked_list_3 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_3) == 0
    bool_0 = False
    dict_0 = {bool_0: singly_linked_list_0}
    var_5 = var_4.append(var_3)
    assert len(singly_linked_list_0) == 3
    assert len(var_2) == 3
    assert len(var_4) == 3
    var_6 = var_4.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 4
    assert len(var_2) == 4
    assert len(var_4) == 4

def test_case_17():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    assert len(singly_linked_list_0) == 0
    var_0 = singly_linked_list_0.append(singly_linked_list_0)
    assert len(singly_linked_list_0) == 1

def test_case_18():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    with pytest.raises(StopIteration):
        doubly_linked_list_0.previous()

def test_case_19():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 2
    var_2 = doubly_linked_list_0.next()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(var_2) == 2
    var_3 = var_2.previous()
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(var_3) == 2
    var_4 = var_3.__len__()
    assert var_4 == 2
    var_5 = var_3.__len__()
    assert var_5 == 2

def test_case_20():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 2
    var_2 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 3

def test_case_21():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 2

def test_case_22():
    int_0 = -2627
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(int_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.append(int_0)
    assert len(doubly_linked_list_0) == 2
    var_2 = doubly_linked_list_0.insert(int_0, int_0)
    assert len(doubly_linked_list_0) == 3
    var_3 = doubly_linked_list_0.append(var_2)
    assert len(doubly_linked_list_0) == 4

def test_case_23():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1

def test_case_24():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    int_0 = -3179
    var_0 = doubly_linked_list_0.insert(int_0, int_0)
    assert len(doubly_linked_list_0) == 1

def test_case_25():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    bool_0 = False
    none_type_0 = None
    var_0 = doubly_linked_list_0.append(none_type_0)
    assert len(doubly_linked_list_0) == 1
    var_1 = doubly_linked_list_0.insert(bool_0, bool_0)
    assert len(doubly_linked_list_0) == 3

def test_case_26():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__len__()
    assert var_0 == 0
    var_1 = doubly_linked_list_0.append(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_2 = doubly_linked_list_0.insert(var_0, var_0)
    assert len(doubly_linked_list_0) == 3

def test_case_27():
    int_0 = -2595
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(int_0)
    assert len(doubly_linked_list_0) == 1

def test_case_28():
    none_type_0 = None
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.append(none_type_0)
    assert len(doubly_linked_list_0) == 1
    bool_0 = False
    doubly_linked_list_1 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_1) == 0
    complex_0 = -4.22462 + 34.2935j
    var_1 = doubly_linked_list_1.__contains__(complex_0)
    var_2 = doubly_linked_list_1.__contains__(complex_0)
    var_3 = doubly_linked_list_1.append(bool_0)
    assert len(doubly_linked_list_1) == 1
    var_4 = doubly_linked_list_1.append(bool_0)
    assert len(doubly_linked_list_1) == 2
    doubly_linked_node_0 = module_0.DoublyLinkedNode(bool_0)
    assert doubly_linked_node_0.prev is None
    doubly_linked_list_2 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_2) == 0
    str_0 = 'Jd#i'
    str_1 = 'RWYrhbFCiOg.Uub5hm`'
    singly_linked_node_0 = module_0.SinglyLinkedNode(str_1)
    var_5 = doubly_linked_list_1.insert(str_0, bool_0)
    assert len(doubly_linked_list_1) == 3

def test_case_29():
    bool_0 = False
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    with pytest.raises(IndexError):
        doubly_linked_list_0.insert(bool_0, bool_0)

def test_case_30():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__len__()
    assert var_0 == 0

def test_case_31():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.__iter__()
    assert len(var_0) == 0

def test_case_32():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    doubly_linked_node_0 = module_0.DoublyLinkedNode(doubly_linked_list_0)
    assert f'{type(doubly_linked_node_0.data).__module__}.{type(doubly_linked_node_0.data).__qualname__}' == 'linkedList1.DoublyLinkedList'
    assert len(doubly_linked_node_0.data) == 0
    assert doubly_linked_node_0.next is None
    assert doubly_linked_node_0.prev is None
