#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack4/DYNAMOSA/test_stack4.py.orig
import pytest
import stack4 as module_0

def test_case_0():
    bool_0 = False
    str_0 = '/A\n'
    stack_0 = module_0.Stack(str_0)
    var_0 = stack_0.push(bool_0)
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None

def test_case_1():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None

def test_case_2():
    int_0 = -904
    set_0 = {int_0, int_0, int_0, int_0}
    linked_list_0 = module_0.LinkedList(set_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.pop()
    assert var_0 == -904
    assert linked_list_0.head is None
    linked_list_1 = module_0.LinkedList()
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_1.head is None
    var_1 = linked_list_1.remove(linked_list_1)
    var_2 = module_0.LinkedList(var_1)
    assert var_2.head is None
    var_3 = linked_list_1.remove(var_1)

def test_case_3():
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'

def test_case_4():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    bool_0 = False
    var_0 = linked_list_0.push(bool_0)
    node_0 = linked_list_0.search(bool_0)
    assert f'{type(node_0).__module__}.{type(node_0).__qualname__}' == 'stack4.Node'
    assert node_0.data is False
    assert node_0.next is None
    tuple_0 = ()
    node_1 = module_0.Node(tuple_0)
    linked_list_1 = module_0.LinkedList()
    assert linked_list_1.head is None
    var_1 = linked_list_1.search(tuple_0)
    stack_0 = module_0.Stack()

def test_case_5():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.remove(linked_list_0)
    var_1 = linked_list_0.size()
    assert var_1 == 0

def test_case_6():
    bool_0 = True
    linked_list_0 = module_0.LinkedList(bool_0)
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.display()
    assert var_0 == '(True)'

def test_case_7():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.display()
    assert var_0 == ')'

def test_case_8():
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    list_0 = [stack_0, stack_0]
    node_0 = module_0.Node(list_0)

def test_case_9():
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'

def test_case_10():
    list_0 = []
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    linked_list_0 = module_0.LinkedList(stack_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.remove(list_0)

def test_case_11():
    bool_0 = True
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    bool_1 = False
    var_0 = linked_list_0.search(bool_1)
    var_1 = linked_list_0.remove(bool_0)
    var_2 = linked_list_0.push(bool_0)
    var_3 = linked_list_0.remove(var_1)
    var_4 = linked_list_0.search(var_3)

def test_case_12():
    bool_0 = True
    tuple_0 = (bool_0,)
    list_0 = [tuple_0, bool_0, tuple_0]
    linked_list_0 = module_0.LinkedList(list_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.size()
    assert var_0 == 3
    var_1 = linked_list_0.display()
    assert var_1 == '((True,), True, (True,))'

def test_case_13():
    bool_0 = True
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.remove(bool_0)
    var_2 = linked_list_0.push(bool_0)
    var_3 = linked_list_0.remove(var_1)
    var_4 = linked_list_0.search(var_3)

def test_case_14():
    bool_0 = True
    bool_1 = True
    none_type_0 = None
    linked_list_0 = module_0.LinkedList(bool_0)
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.search(bool_0)
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'stack4.Node'
    assert var_0.data is True
    assert var_0.next is None
    var_1 = linked_list_0.remove(bool_1)
    assert linked_list_0.head is None
    list_0 = [none_type_0, var_1]

def test_case_15():
    bool_0 = True
    int_0 = 13
    bool_1 = True
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = module_0.Node(bool_1)
    var_1 = linked_list_0.push(int_0)
    var_2 = linked_list_0.remove(bool_0)
    var_3 = linked_list_0.push(bool_0)
    var_4 = linked_list_0.remove(var_2)
    var_5 = linked_list_0.remove(int_0)
