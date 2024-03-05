#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList2/MOSA/test_linkedList2.py.orig
import pytest
import linkedList2 as module_0

def test_case_0():
    int_0 = -1270
    linked_node_0 = module_0.LinkedNode(int_0)
    var_0 = linked_node_0.checkInfinite()
    assert var_0 is False

def test_case_1():
    bool_0 = False
    linked_node_0 = module_0.LinkedNode(bool_0, bool_0)

def test_case_2():
    none_type_0 = None
    list_0 = [none_type_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 1

def test_case_3():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__len__()
    assert var_0 == 0
    var_1 = linked_list_0.prepend(var_0)
    assert len(linked_list_0) == 1

def test_case_4():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__repr__()
    assert var_0 == 'link:[]'
    with pytest.raises(Exception):
        linked_list_0.pop()

def test_case_5():
    bytes_0 = b'\x14\x0f\xf4'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 4
    str_0 = "'_*"
    list_1 = [str_0]
    linked_list_1 = module_0.LinkedList(*list_1)
    assert len(linked_list_1) == 1
    var_0 = linked_list_1.pop()
    assert var_0 == "'_*"
    assert len(linked_list_1) == 0
    var_1 = var_0.__len__()

def test_case_6():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.remove(linked_list_0)
    assert var_1 is True
    assert len(linked_list_0) == 0

def test_case_7():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__iter__()
    var_1 = var_0.__repr__()
    var_2 = var_1.__repr__()
    var_3 = linked_list_0.remove(var_0)
    assert var_3 is False

def test_case_8():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_node_0 = module_0.LinkedNode(linked_list_0)
    assert len(linked_node_0.value) == 0
    none_type_0 = None
    var_0 = linked_list_0.remove(none_type_0)
    assert var_0 is False
    var_1 = linked_list_0.__len__()
    assert var_1 == 0
    var_2 = linked_list_0.prepend(none_type_0)
    assert len(linked_list_0) == 1
    assert len(linked_node_0.value) == 1
    var_3 = linked_list_0.prepend(var_1)
    assert len(linked_list_0) == 2
    assert len(linked_node_0.value) == 2
    linked_node_1 = module_0.LinkedNode(linked_list_0, linked_node_0)
    assert len(linked_node_1.value) == 2
    var_4 = linked_node_1.checkInfinite()
    assert var_4 is False
    linked_list_1 = module_0.LinkedList(*linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'linkedList2.LinkedList'
    assert len(linked_list_1) == 2
    var_5 = linked_list_0.remove(var_4)
    assert var_5 is True
    assert len(linked_list_0) == 1
    assert len(linked_node_0.value) == 1
    assert len(linked_node_1.value) == 1

def test_case_9():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_node_0 = module_0.LinkedNode(linked_list_0)
    assert len(linked_node_0.value) == 0
    var_0 = linked_list_0.__len__()
    assert var_0 == 0
    var_1 = linked_list_0.prepend(var_0)
    assert len(linked_list_0) == 1
    assert len(linked_node_0.value) == 1
    linked_list_1 = module_0.LinkedList(*linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'linkedList2.LinkedList'
    assert len(linked_list_1) == 1
    var_2 = linked_list_0.remove(var_0)
    assert var_2 is True
    assert len(linked_list_0) == 0
    assert len(linked_node_0.value) == 0

def test_case_10():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__repr__()
    assert var_0 == 'link:[]'
    var_1 = var_0.__len__()
    assert var_1 == 7
    var_2 = var_0.__iter__()

def test_case_11():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_node_0 = module_0.LinkedNode(linked_list_0)
    assert len(linked_node_0.value) == 0
    var_0 = linked_list_0.__len__()
    assert var_0 == 0
    var_1 = linked_list_0.prepend(var_0)
    assert len(linked_list_0) == 1
    assert len(linked_node_0.value) == 1
    linked_list_1 = module_0.LinkedList(*linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'linkedList2.LinkedList'
    assert len(linked_list_1) == 1
    var_2 = linked_list_1.__repr__()
    assert var_2 == 'link:[0]'
    var_3 = linked_list_0.remove(var_0)
    assert var_3 is True
    assert len(linked_list_0) == 0
    assert len(linked_node_0.value) == 0

def test_case_12():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__repr__()
    assert var_0 == 'link:[]'
    var_1 = var_0.__len__()
    assert var_1 == 7
    linked_list_1 = module_0.LinkedList(*var_0)
    assert len(linked_list_1) == 7
    var_2 = linked_list_1.remove(linked_list_1)
    assert var_2 is False
    var_3 = linked_list_1.remove(var_1)
    assert var_3 is False

def test_case_13():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_node_0 = module_0.LinkedNode(linked_list_0)
    assert len(linked_node_0.value) == 0
    linked_node_1 = module_0.LinkedNode(linked_list_0, linked_node_0)
    assert len(linked_node_1.value) == 0
    var_0 = linked_node_1.checkInfinite()
    assert var_0 is False
    linked_list_1 = module_0.LinkedList(*linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'linkedList2.LinkedList'
    assert len(linked_list_1) == 0
    var_1 = var_0.__repr__()
    assert var_1 == 'False'

def test_case_14():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_node_0 = module_0.LinkedNode(linked_list_0)
    assert len(linked_node_0.value) == 0
    linked_node_1 = module_0.LinkedNode(linked_list_0, linked_node_0)
    assert len(linked_node_1.value) == 0
    var_0 = linked_node_1.checkInfinite()
    assert var_0 is False

def test_case_15():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_node_0 = module_0.LinkedNode(linked_list_0)
    assert len(linked_node_0.value) == 0
    str_0 = "B}#(.|'P}9n)Ya*a"
    var_0 = linked_list_0.__len__()
    assert var_0 == 0
    var_1 = module_0.LinkedNode(linked_list_0, str_0)
    assert len(var_1.value) == 0
    linked_node_1 = module_0.LinkedNode(linked_node_0, var_1)
