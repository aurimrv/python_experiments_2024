#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack5/WHOLE_SUITE/test_stack5.py
import pytest
import stack5 as module_0
import builtins as module_1

def test_case_0():
    none_type_0 = None
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(none_type_0)
    stack_1 = module_0.Stack()
    var_1 = stack_1.pop()
#    var_1.is_empty()

def test_case_1():
    list_0 = []
    object_0 = module_1.object(*list_0)
    stack_0 = module_0.Stack(object_0)
    int_0 = -3620
    tuple_0 = (int_0, int_0)
    stack_1 = module_0.Stack(tuple_0)
    node_0 = module_0.Node(stack_1, int_0)
    stack_2 = module_0.Stack()
    var_0 = stack_2.pop()
#    var_0.pop()

def test_case_2():
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(stack_0)
    var_1 = stack_0.is_empty()
    var_2 = stack_0.pop()
    assert stack_0.top is None
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'stack5.Stack'
    assert var_2.top is None
    var_3 = var_2.pop()
    var_4 = var_2.pop()
#    var_1.pop()

def test_case_3():
    bool_0 = True
    stack_0 = module_0.Stack(bool_0)

def test_case_4():
    stack_0 = module_0.Stack()
    none_type_0 = None
    var_0 = stack_0.push(none_type_0)
    node_0 = module_0.Node(stack_0, none_type_0)
    node_1 = module_0.Node(stack_0)
    stack_1 = module_0.Stack()
    node_2 = module_0.Node(none_type_0, node_1)
    var_1 = stack_0.is_empty()
    var_2 = stack_1.peek()
    stack_2 = module_0.Stack(var_2)
    var_3 = stack_0.is_empty()
    stack_3 = module_0.Stack(var_3)
    var_4 = stack_1.is_empty()

def test_case_5():
    none_type_0 = None
    stack_0 = module_0.Stack(none_type_0)
    stack_1 = module_0.Stack(none_type_0)
    var_0 = stack_0.is_empty()
    stack_2 = module_0.Stack()
    var_1 = stack_2.pop()
    node_0 = module_0.Node(stack_0)
    var_2 = stack_1.pop()
    var_3 = stack_2.pop()
#    var_3.pop()

def test_case_6():
    bytes_0 = b"\xfa\xa2\x19\xb25\x05!\x07o7\xa6O\n\x854j\xd6'\x13\xfa"
    dict_0 = {bytes_0: bytes_0}
    list_0 = [dict_0, dict_0]
    stack_0 = module_0.Stack(list_0)
