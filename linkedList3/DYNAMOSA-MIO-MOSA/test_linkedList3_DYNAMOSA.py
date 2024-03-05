#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList3/DYNAMOSA/test_linkedList3.py.orig
import pytest
import linkedList3 as module_0

def test_case_0():
    singly_linked_list_0 = module_0.SinglyLinkedList()

def test_case_1():
    str_0 = '+(ff'
    singly_linked_list_0 = module_0.SinglyLinkedList()
    none_type_0 = singly_linked_list_0.add(str_0)
    var_0 = singly_linked_list_0.remove()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList3.Node'
    assert var_0.value == '+(ff'
    assert var_0.next is None

def test_case_2():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    var_0 = singly_linked_list_0.remove()
    node_0 = module_0.Node(var_0)
    assert node_0.value is None
    singly_linked_list_1 = module_0.SinglyLinkedList()
    none_type_0 = singly_linked_list_1.add(singly_linked_list_1)
    int_0 = singly_linked_list_1.getSize()
    assert int_0 == 1
    int_1 = singly_linked_list_1.getSize()
    assert int_1 == 1
    var_1 = singly_linked_list_1.getHead()
    var_2 = singly_linked_list_1.getHead()
    node_1 = singly_linked_list_0.getHeadNode()
    assert f'{type(node_1).__module__}.{type(node_1).__qualname__}' == 'linkedList3.Node'
    assert node_1.value is None
    assert node_1.next is None
    node_2 = singly_linked_list_0.getHeadNode()
    assert f'{type(node_2).__module__}.{type(node_2).__qualname__}' == 'linkedList3.Node'
    assert node_2.value is None
    assert node_2.next is None
    int_2 = singly_linked_list_1.getSize()
    assert int_2 == 1
    int_3 = singly_linked_list_1.getSize()
    assert int_3 == 1
    str_0 = singly_linked_list_0.__str__()
    assert str_0 == '[None]'
    bool_0 = singly_linked_list_1.isEmpty()
    assert bool_0 is False
    none_type_1 = var_2.add(int_3)
    bool_1 = singly_linked_list_0.isEmpty()
    assert bool_1 is True
    node_3 = singly_linked_list_1.getHeadNode()
    assert node_3.value == 1
    assert f'{type(node_3.next).__module__}.{type(node_3.next).__qualname__}' == 'linkedList3.Node'
    singly_linked_list_2 = module_0.SinglyLinkedList()
    var_3 = singly_linked_list_2.getHead()
    list_0 = singly_linked_list_1.toArray()

def test_case_3():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    var_0 = singly_linked_list_0.remove()

def test_case_4():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    list_0 = singly_linked_list_0.toArray()
    var_0 = singly_linked_list_0.getHead()
    str_0 = singly_linked_list_0.__str__()
    assert str_0 == '[None]'
    bool_0 = singly_linked_list_0.isEmpty()
    assert bool_0 is True

def test_case_5():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    list_0 = singly_linked_list_0.toArray()

def test_case_6():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    str_0 = singly_linked_list_0.__str__()
    assert str_0 == '[None]'

def test_case_7():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    str_0 = singly_linked_list_0.getHead()

def test_case_8():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    node_0 = singly_linked_list_0.getHeadNode()

def test_case_9():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    int_0 = singly_linked_list_0.getSize()

def test_case_10():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    bool_0 = singly_linked_list_0.isEmpty()
    assert bool_0 is True
    bool_1 = singly_linked_list_0.isEmpty()
    assert bool_1 is True
    list_0 = singly_linked_list_0.toArray()
    singly_linked_list_1 = module_0.SinglyLinkedList()
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    bool_2 = singly_linked_list_0.isEmpty()
    assert bool_2 is False
    node_0 = module_0.Node(singly_linked_list_0)
    node_1 = module_0.Node(node_0)
    none_type_1 = singly_linked_list_0.add(singly_linked_list_0)
    list_1 = []
    bool_3 = singly_linked_list_0.isEmpty()
    assert bool_3 is False
    none_type_2 = singly_linked_list_0.add(list_1)
    list_2 = singly_linked_list_0.toArray()
    int_0 = singly_linked_list_0.getSize()
    assert int_0 == 3
    bool_4 = singly_linked_list_0.isEmpty()
    assert bool_4 is False
    singly_linked_list_2 = module_0.SinglyLinkedList()
    none_type_3 = singly_linked_list_0.add(singly_linked_list_2)
    var_0 = singly_linked_list_0.getHead()
    var_1 = var_0.remove()
    str_0 = singly_linked_list_0.__str__()
    var_2 = var_0.remove()
    none_type_4 = var_0.add(int_0)
