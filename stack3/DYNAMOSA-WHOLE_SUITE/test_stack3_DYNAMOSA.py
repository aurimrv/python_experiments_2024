#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack3/DYNAMOSA/test_stack3.py.orig
import pytest
import stack3 as module_0

def test_case_0():
    stack_0 = module_0.Stack()

def test_case_1():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    var_0 = singly_linked_list_0.remove()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'stack3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'stack3.SinglyLinkedList'
    assert var_0.next is None

def test_case_2():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    int_0 = singly_linked_list_0.getSize()
    stack_0 = module_0.Stack()
    var_0 = singly_linked_list_0.remove()

def test_case_3():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    bool_0 = singly_linked_list_0.isEmpty()
    assert bool_0 is True
    var_0 = singly_linked_list_0.remove()

def test_case_4():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    node_0 = singly_linked_list_0.getHeadNode()
    int_0 = singly_linked_list_0.getSize()
    list_0 = singly_linked_list_0.toArray()
    none_type_0 = singly_linked_list_0.add(list_0)
    bool_0 = singly_linked_list_0.isEmpty()
    assert bool_0 is False
    var_0 = singly_linked_list_0.remove()
    assert node_0.next is None
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'stack3.Node'
    assert var_0.value == [None]
    assert var_0.next is None
    str_0 = list_0.__str__()
    assert str_0 == '[None]'
    node_1 = module_0.Node(bool_0)
    assert node_1.value is False

def test_case_5():
    stack_0 = module_0.Stack()
    str_0 = stack_0.__str__()
    assert str_0 == '[None]'

def test_case_6():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    str_0 = singly_linked_list_0.__str__()
    assert str_0 == '[None]'

def test_case_7():
    stack_0 = module_0.Stack()
    bool_0 = stack_0.isEmpty()
    assert bool_0 is True
    var_0 = stack_0.pop()

def test_case_8():
    int_0 = 4462
    node_0 = module_0.Node(int_0)
    singly_linked_list_0 = module_0.SinglyLinkedList()
    var_0 = singly_linked_list_0.getHead()

def test_case_9():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    str_0 = singly_linked_list_0.__str__()
    var_0 = singly_linked_list_0.remove()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'stack3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'stack3.SinglyLinkedList'
    assert var_0.next is None
    node_0 = singly_linked_list_0.getHeadNode()
    assert f'{type(node_0).__module__}.{type(node_0).__qualname__}' == 'stack3.Node'
    assert node_0.value is None
    assert node_0.next is None

def test_case_10():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    stack_0 = module_0.Stack()
    bool_0 = False
    none_type_0 = singly_linked_list_0.add(bool_0)
    none_type_1 = stack_0.push(singly_linked_list_0)
    var_0 = singly_linked_list_0.remove()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'stack3.Node'
    assert var_0.value is False
    assert var_0.next is None

def test_case_11():
    stack_0 = module_0.Stack()
    var_0 = stack_0.peek()

def test_case_12():
    stack_0 = module_0.Stack()
    str_0 = stack_0.__str__()
    assert str_0 == '[None]'
    var_0 = stack_0.peek()
    int_0 = stack_0.getSize()

def test_case_13():
    stack_0 = module_0.Stack()
    none_type_0 = stack_0.push(stack_0)
    var_0 = stack_0.peek()
    bool_0 = var_0.isEmpty()
    assert bool_0 is False
    stack_1 = module_0.Stack()
    var_1 = stack_0.pop()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'stack3.Node'
    assert f'{type(var_1.value).__module__}.{type(var_1.value).__qualname__}' == 'stack3.Stack'
    assert var_1.next is None
    var_2 = stack_0.peek()

def test_case_14():
    stack_0 = module_0.Stack()
    int_0 = stack_0.peek()
    none_type_0 = stack_0.push(stack_0)
    none_type_1 = stack_0.push(stack_0)
    var_0 = module_0.SinglyLinkedList()
    var_1 = var_0.getHead()
    var_2 = stack_0.peek()
    var_3 = var_2.peek()

def test_case_15():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    list_0 = singly_linked_list_0.toArray()
    str_0 = singly_linked_list_0.__str__()
    assert str_0 == '[None]'
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    bool_0 = singly_linked_list_0.isEmpty()
    assert bool_0 is False
    none_type_1 = singly_linked_list_0.add(list_0)
    bool_1 = singly_linked_list_0.isEmpty()
    assert bool_1 is False
    list_1 = singly_linked_list_0.toArray()
    var_0 = singly_linked_list_0.remove()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'stack3.Node'
    assert var_0.value == [None]
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'stack3.Node'

def test_case_16():
    singly_linked_list_0 = module_0.SinglyLinkedList()
    list_0 = singly_linked_list_0.toArray()
    str_0 = singly_linked_list_0.__str__()
    assert str_0 == '[None]'
    none_type_0 = singly_linked_list_0.add(singly_linked_list_0)
    none_type_1 = singly_linked_list_0.add(str_0)
    str_1 = singly_linked_list_0.__str__()
    bool_0 = singly_linked_list_0.isEmpty()
    assert bool_0 is False
    int_0 = singly_linked_list_0.getSize()
    assert int_0 == 2
    var_0 = singly_linked_list_0.remove()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'stack3.Node'
    assert var_0.value == '[None]'
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'stack3.Node'
