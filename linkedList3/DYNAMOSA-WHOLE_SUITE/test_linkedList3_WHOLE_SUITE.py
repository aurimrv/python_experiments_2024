#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList3/WHOLE_SUITE/test_linkedList3.py.orig
import pytest
import linkedList3 as module_0

def test_case_0():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    none_type_1 = singly_linked_list_0.add(singly_linked_list_0)
    node_0 = singly_linked_list_0.getHeadNode()
    singly_linked_list_1 = module_0.SinglyLinkedList()
    node_1 = module_0.Node(singly_linked_list_1)
    none_type_2 = singly_linked_list_0.add(singly_linked_list_1)
    node_2 = module_0.Node(none_type_2)

def test_case_1():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    var_0 = singly_linked_list_0.remove()

def test_case_2():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    node_0 = singly_linked_list_0.getHeadNode()
    node_1 = singly_linked_list_0.getHeadNode()
    none_type_0 = singly_linked_list_0.add(node_1)
    var_0 = singly_linked_list_0.remove()
    assert node_0.next is None
    assert node_1.next is None
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'linkedList3.Node'
    assert var_0.next is None
    singly_linked_list_1 = module_0.SinglyLinkedList()
    node_2 = module_0.Node(var_0)
    assert f'{type(node_2.value).__module__}.{type(node_2.value).__qualname__}' == 'linkedList3.Node'
    int_0 = singly_linked_list_1.getSize()
    var_1 = singly_linked_list_1.getHead()
    list_0 = singly_linked_list_1.toArray()
    var_2 = singly_linked_list_0.remove()
    var_3 = singly_linked_list_0.remove()

def test_case_3():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    complex_0 = -1570.48195 - 1139.15j
    none_type_0 = singly_linked_list_0.add(complex_0)
    int_0 = singly_linked_list_0.getSize()
    assert int_0 == 1
    none_type_1 = singly_linked_list_0.add(singly_linked_list_0)
    list_0 = singly_linked_list_0.toArray()
    int_1 = singly_linked_list_0.getSize()
    assert int_1 == 2
    node_0 = singly_linked_list_0.getHeadNode()
    node_1 = singly_linked_list_0.getHeadNode()
    var_0 = singly_linked_list_0.getHead()
    int_2 = singly_linked_list_0.getSize()
    assert int_2 == 2
    list_1 = singly_linked_list_0.toArray()
    var_1 = singly_linked_list_0.getHead()
    var_2 = singly_linked_list_0.remove()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList3.Node'
    assert f'{type(var_2.value).__module__}.{type(var_2.value).__qualname__}' == 'linkedList3.SinglyLinkedList'
    assert f'{type(var_2.next).__module__}.{type(var_2.next).__qualname__}' == 'linkedList3.Node'
    node_2 = module_0.Node(node_1)
    var_3 = var_1.remove()
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList3.Node'
    assert var_3.value is None
    assert var_3.next is None
    node_3 = singly_linked_list_0.getHeadNode()
    assert f'{type(node_3).__module__}.{type(node_3).__qualname__}' == 'linkedList3.Node'
    assert node_3.value is None
    assert node_3.next is None
    node_4 = module_0.Node(none_type_1)
    list_2 = var_1.toArray()

def test_case_4():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    bool_0 = singly_linked_list_0.isEmpty()
    assert bool_0 is True
    var_0 = singly_linked_list_0.remove()
    node_0 = singly_linked_list_0.getHeadNode()
    assert f'{type(node_0).__module__}.{type(node_0).__qualname__}' == 'linkedList3.Node'
    assert node_0.value is None
    assert node_0.next is None

def test_case_5():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    var_0 = singly_linked_list_0.remove()

def test_case_6():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    list_0 = singly_linked_list_0.toArray()
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    none_type_1 = singly_linked_list_0.add(singly_linked_list_0)
    node_0 = singly_linked_list_0.getHeadNode()
    int_0 = singly_linked_list_0.getSize()
    assert int_0 == 2
    str_0 = singly_linked_list_0.__str__()
    list_1 = singly_linked_list_0.toArray()
    list_2 = singly_linked_list_0.toArray()
    int_1 = singly_linked_list_0.getSize()
    assert int_1 == 2
    var_0 = singly_linked_list_0.remove()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'linkedList3.SinglyLinkedList'
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList3.Node'

def test_case_7():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    list_0 = singly_linked_list_0.toArray()
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    none_type_1 = singly_linked_list_0.add(singly_linked_list_0)
    node_0 = singly_linked_list_0.getHeadNode()
    int_0 = singly_linked_list_0.getSize()
    assert int_0 == 2
    singly_linked_list_1 = module_0.SinglyLinkedList()
    str_0 = singly_linked_list_1.__str__()
    assert str_0 == '[None]'
    list_1 = singly_linked_list_0.toArray()
    list_2 = singly_linked_list_1.toArray()
    int_1 = singly_linked_list_1.getSize()
    int_2 = singly_linked_list_1.getSize()
    var_0 = singly_linked_list_1.remove()
    node_1 = singly_linked_list_1.getHeadNode()
    assert f'{type(node_1).__module__}.{type(node_1).__qualname__}' == 'linkedList3.Node'
    assert node_1.value is None
    assert node_1.next is None
    str_1 = var_0.__str__()
    assert str_1 == 'None'
    singly_linked_list_2 = module_0.SinglyLinkedList()
    str_2 = singly_linked_list_1.__str__()
    assert str_2 == '[None]'
    none_type_2 = singly_linked_list_2.add(int_2)
    node_2 = singly_linked_list_1.getHeadNode()
    assert f'{type(node_2).__module__}.{type(node_2).__qualname__}' == 'linkedList3.Node'
    assert node_2.value is None
    assert node_2.next is None
    str_3 = singly_linked_list_2.__str__()
    assert str_3 == '[0]'
    int_3 = singly_linked_list_0.getSize()
    assert int_3 == 2
    int_4 = singly_linked_list_2.getSize()
    assert int_4 == 1
    int_5 = singly_linked_list_1.getSize()
    assert int_5 == 0
    bool_0 = singly_linked_list_2.isEmpty()
    assert bool_0 is False
    int_6 = singly_linked_list_2.getSize()
    assert int_6 == 1
    str_4 = singly_linked_list_1.__str__()
    assert str_4 == '[None]'
    node_3 = singly_linked_list_2.getHeadNode()
