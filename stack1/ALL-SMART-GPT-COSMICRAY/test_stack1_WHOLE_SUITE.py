#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack1/WHOLE_SUITE/test_stack1.py.orig
import pytest
import stack1 as module_0

def test_case_0():
    str_0 = '+'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is True
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_1():
    float_0 = -1074.68
    stack_node_0 = module_0.StackNode(float_0)
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    stack_node_1 = module_0.StackNode(stack_0)
    assert len(stack_node_1.data) == 0
    stack_1 = module_0.Stack()
    assert len(stack_1) == 0
    var_0 = stack_1.push(stack_1)
    assert len(stack_1) == 1
    var_1 = stack_1.push(float_0)
    assert len(stack_1) == 2
    var_2 = stack_1.peek()
    assert var_2 == pytest.approx(-1074.68, abs=0.01, rel=0.01)

def test_case_2():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    stack_1 = module_0.Stack()
    assert len(stack_1) == 0
    var_0 = stack_1.push(stack_1)
    assert len(stack_1) == 1
    var_1 = stack_1.__len__()
    assert var_1 == 1
    with pytest.raises(ValueError):
        stack_0.peek()

def test_case_3():
    set_0 = set()
    none_type_0 = None

def test_case_4():
    set_0 = set()

def test_case_5():
    str_0 = '%V[^8\x0b3#niiMS&'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False

def test_case_6():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0

def test_case_7():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    str_0 = 'Eo(l<,t{Sl=T`'
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_8():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    str_0 = 'Eo(l<,t{Sl=T`'
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_9():
    str_0 = 'K*{g\\\nq1p\\j~,7`]'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    var_1 = stack_0.__len__()
    assert var_1 == 0
    with pytest.raises(ValueError):
        stack_0.pop()

def test_case_10():
    str_0 = 'a"e{v#}1l$1\rqjR!'
    stack_node_0 = module_0.StackNode(str_0)

def test_case_11():
    str_0 = 'a"e{v#}1l$1\rqjR!'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is True

def test_case_12():
    str_0 = 'a"e{v#}1l$1\rqjR!'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is True

def test_case_13():
    str_0 = 'W\t\rwj}KJ9'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False
    var_1 = module_0.check_parenthesis(str_0)
    assert var_1 is False

def test_case_14():
    str_0 = '3'
    stack_node_0 = module_0.StackNode(str_0)
    var_0 = module_0.postfix_eval(str_0)
    assert var_0 == 3
    var_1 = module_0.postfix_eval(str_0)

def test_case_15():
    str_0 = '7Z.\x0b)}0\t(`K`VY~;4'
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_16():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    with pytest.raises(ValueError):
        stack_0.pop()
