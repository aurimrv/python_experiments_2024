#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack2/MOSA/test_stack2.py.orig
import pytest
import stack2 as module_0

def test_case_0():
    stack_0 = module_0.Stack()
    with pytest.raises(Exception):
        stack_0.pop()

def test_case_1():
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(stack_0)
    stack_1 = module_0.Stack()
    var_1 = stack_1.push(stack_1)
    var_2 = stack_1.pop()
    assert stack_1.stack == []
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'stack2.Stack'
    assert var_2.stack == []
    var_3 = stack_1.push(stack_0)
    stack_2 = module_0.Stack()
    stack_3 = module_0.Stack()
    var_4 = var_3.__repr__()
    stack_4 = module_0.Stack()
    with pytest.raises(Exception):
        stack_4.pop()

def test_case_2():
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(stack_0)

def test_case_3():
    bool_0 = True
    stack_0 = module_0.Stack()
    var_0 = stack_0.isEmpty()
    assert var_0 is True

def test_case_4():
    stack_0 = module_0.Stack()
    var_0 = stack_0.__repr__()
    assert var_0 == 'stack:[]'
