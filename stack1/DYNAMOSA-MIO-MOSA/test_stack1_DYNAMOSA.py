#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack1/DYNAMOSA/test_stack1.py.orig
import pytest
import stack1 as module_0

def test_case_0():
    str_0 = '6'
    var_0 = module_0.postfix_eval(str_0)
    assert var_0 == 6

def test_case_1():
    str_0 = 'R\rip0|*r^)WN&\x0cVl=Z1\x0b'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False

def test_case_2():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    with pytest.raises(ValueError):
        stack_0.peek()

def test_case_3():
    str_0 = '/'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is True
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_4():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0

def test_case_5():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    stack_1 = module_0.Stack()
    assert len(stack_1) == 0
    var_0 = stack_1.__len__()
    assert var_0 == 0
    with pytest.raises(ValueError):
        stack_1.peek()

def test_case_6():
    str_0 = 'dLrqj0=`{6N&8'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False
    str_1 = '%'
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_1)

def test_case_7():
    str_0 = 'qtOO",O"%dY}IZ~C?r'
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_8():
    str_0 = '6'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is True
    var_1 = str_0.__len__()
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    var_2 = stack_0.push(var_1)
    assert len(stack_0) == 1
    var_3 = stack_0.push(stack_0)
    assert len(stack_0) == 2

def test_case_9():
    str_0 = '6'
    var_0 = module_0.Stack()
    assert len(var_0) == 0
    var_1 = module_0.check_parenthesis(str_0)
    assert var_1 is True
    var_2 = var_0.push(var_0)
    assert len(var_0) == 1
    var_3 = var_0.peek()
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'stack1.Stack'
    assert len(var_3) == 1
    var_4 = var_0.push(var_0)
    assert len(var_0) == 2
    assert len(var_3) == 2

def test_case_10():
    str_0 = 'LLX@-!\tU(4:;(]U'
    var_0 = module_0.StackNode(str_0)
    stack_node_0 = module_0.StackNode(str_0)
    var_1 = module_0.check_parenthesis(str_0)
    assert var_1 is False

def test_case_11():
    str_0 = '(T lON)_'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is True
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_12():
    str_0 = '/'
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)
