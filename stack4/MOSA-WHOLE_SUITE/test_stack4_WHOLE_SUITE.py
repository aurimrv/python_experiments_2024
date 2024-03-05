#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack4/WHOLE_SUITE/test_stack4.py.orig
import pytest
import stack4 as module_0

def test_case_0():
    str_0 = ''
    stack_0 = module_0.Stack(str_0)
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    linked_list_1 = module_0.LinkedList()
    assert linked_list_1.head is None
    var_0 = linked_list_0.search(linked_list_1)
    linked_list_2 = module_0.LinkedList()
    assert linked_list_2.head is None
    stack_1 = module_0.Stack()
    var_1 = linked_list_2.display()
    assert var_1 == ')'
    var_2 = linked_list_2.remove(linked_list_0)
    var_3 = linked_list_0.search(linked_list_2)
    var_4 = linked_list_2.push(var_2)
    var_5 = linked_list_2.push(var_2)
    var_6 = linked_list_2.remove(var_2)

def test_case_1():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    node_0 = module_0.Node(linked_list_0)
    bytes_0 = b'\x8f/\xa1K\x98\x16)\xf1l7Zf\x8a\xfc\xe8 \xcf'
    var_0 = linked_list_0.push(bytes_0)
    node_1 = module_0.Node(linked_list_0, linked_list_0)
    var_1 = linked_list_0.push(node_1)
    var_2 = linked_list_0.search(linked_list_0)
    linked_list_1 = module_0.LinkedList()
    assert linked_list_1.head is None
    var_3 = linked_list_0.display()

def test_case_2():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    linked_list_1 = module_0.LinkedList(linked_list_0)
    assert f'{type(linked_list_1.head).__module__}.{type(linked_list_1.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_1.search(linked_list_0)
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'stack4.Node'
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'stack4.LinkedList'
    assert var_0.next is None
    var_1 = linked_list_0.display()
    assert var_1 == ')'

def test_case_3():
    float_0 = 1356.0
    node_0 = module_0.Node(float_0)
    bool_0 = False
    node_1 = module_0.Node(bool_0)
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    node_2 = module_0.Node(float_0)
    var_0 = linked_list_0.size()
    assert var_0 == 0
    linked_list_1 = module_0.LinkedList()
    assert linked_list_1.head is None
    with pytest.raises(IndexError):
        linked_list_1.pop()

def test_case_4():
    float_0 = 1356.0
    none_type_0 = None
    node_0 = module_0.Node(none_type_0)
    bool_0 = False
    node_1 = module_0.Node(bool_0)
    node_2 = module_0.Node(float_0)
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    with pytest.raises(IndexError):
        linked_list_0.pop()

def test_case_5():
    str_0 = 'z\x0b'
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.remove(str_0)
    node_0 = module_0.Node(linked_list_0, linked_list_0)
    var_1 = linked_list_0.remove(str_0)
    var_2 = linked_list_0.push(str_0)
    linked_list_1 = module_0.LinkedList()
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_1.head is None

def test_case_6():
    bool_0 = False
    bool_1 = True
    stack_0 = module_0.Stack(bool_1)
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    var_0 = stack_0.pop()
    var_1 = stack_0.push(bool_0)

def test_case_7():
    none_type_0 = None
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'

def test_case_8():
    int_0 = 1
    stack_0 = module_0.Stack(int_0)
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    var_0 = stack_0.push(int_0)
