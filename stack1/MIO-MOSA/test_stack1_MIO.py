#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack1/MIO/test_stack1.py.orig
import pytest
import stack1 as module_0

def test_case_0():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    var_0 = stack_0.push(stack_0)
    assert len(stack_0) == 1

def test_case_1():
    str_0 = 'p(hy;{K\nEB];*A}L\\'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False

def test_case_2():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    with pytest.raises(ValueError):
        stack_0.pop()

def test_case_3():
    str_0 = '4'
    var_0 = module_0.postfix_eval(str_0)
    assert var_0 == 4

def test_case_4():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    with pytest.raises(ValueError):
        stack_0.peek()

def test_case_5():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    var_0 = stack_0.push(stack_0)
    assert len(stack_0) == 1
    var_1 = stack_0.peek()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'stack1.Stack'
    assert len(var_1) == 1

def test_case_6():
    str_0 = 'b#:{&1y=1zRW~A-l9@@y'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False

def test_case_7():
    str_0 = '}'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False

def test_case_8():
    str_0 = '+J\x0c(]a~lH\n#jd3)*-k&['
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is False

def test_case_9():
    str_0 = '1~ZY[]TI0m%"BbE3G^'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is True

def test_case_10():
    str_0 = '\\=m'
    var_0 = module_0.check_parenthesis(str_0)
    assert var_0 is True

def test_case_11():
    str_0 = "y{7'|-D6V"
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_12():
    str_0 = '/'
    with pytest.raises(ValueError):
        module_0.postfix_eval(str_0)

def test_case_13():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0

def test_case_14():
    stack_0 = module_0.Stack()
    assert len(stack_0) == 0
    var_0 = stack_0.__len__()
    assert var_0 == 0
