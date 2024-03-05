#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack5/DYNAMOSA/test_stack5.py
import pytest
import stack5 as module_0

def test_case_0():
    stack_0 = module_0.Stack()
    var_0 = stack_0.pop()

def test_case_1():
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(stack_0)
    var_1 = stack_0.pop()
    assert stack_0.top is None
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'stack5.Stack'
    assert var_1.top is None
    var_2 = stack_0.push(var_1)
    assert f'{type(var_1.top).__module__}.{type(var_1.top).__qualname__}' == 'stack5.Node'

def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    stack_0 = module_0.Stack(list_0)

def test_case_3():
    stack_0 = module_0.Stack()
    var_0 = stack_0.peek()

def test_case_4():
    bytes_0 = b'\x94\xc5\xfeh^\xfcI\x14\xdc\xbeR\x8f'
    int_0 = -437
    stack_0 = module_0.Stack(int_0)
    var_0 = stack_0.push(bytes_0)

def test_case_5():
    stack_0 = module_0.Stack()
    var_0 = stack_0.pop()
    none_type_0 = None
    var_1 = stack_0.is_empty()
    node_0 = module_0.Node(none_type_0)
    stack_1 = module_0.Stack(none_type_0)
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    node_1 = module_0.Node(stack_0)
    var_2 = stack_0.peek()
    var_3 = stack_3.pop()
