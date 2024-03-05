#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack4/MIO/test_stack4.py.orig
import pytest
import stack4 as module_0

def test_case_0():
    str_0 = 'G0BByujKc^c[c+'
    stack_0 = module_0.Stack(str_0)

def test_case_1():
    set_0 = set()
    linked_list_0 = module_0.LinkedList(set_0)

def test_case_2():
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    linked_list_0 = module_0.LinkedList(stack_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'

def test_case_3():
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'

def test_case_4():
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    var_0 = stack_0.push(stack_0)
    var_1 = stack_0.pop()

def test_case_5():
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'

def test_case_6():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.search(linked_list_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'stack4.Node'
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'stack4.LinkedList'
    assert var_1.next is None

def test_case_7():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.search(var_0)

def test_case_8():
    str_0 = 'bn\tyARa`$?WRR@6]n@'
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.search(str_0)

def test_case_9():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.search(linked_list_0)

def test_case_10():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.push(linked_list_0)
    var_2 = linked_list_0.remove(linked_list_0)

def test_case_11():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.remove(var_0)

def test_case_12():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    linked_list_1 = module_0.LinkedList(linked_list_0)
    assert f'{type(linked_list_1.head).__module__}.{type(linked_list_1.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_1.remove(linked_list_0)
    assert linked_list_1.head is None

def test_case_13():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.remove(linked_list_0)

def test_case_14():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.push(linked_list_0)
    var_2 = linked_list_0.remove(var_1)

def test_case_15():
    str_0 = 'j\tml:RED=@\t\r\x0c/ev'
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.display()
    assert var_0 == '(v, e, /, \x0c, \r, \t, @, =, D, E, R, :, l, m, \t, j)'

def test_case_16():
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    linked_list_0 = module_0.LinkedList(stack_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.display()

def test_case_17():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.display()
    assert var_0 == ')'

def test_case_18():
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    var_0 = stack_0.push(stack_0)

def test_case_19():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.size()
    assert var_0 == 0
