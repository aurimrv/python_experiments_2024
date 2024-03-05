#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack4/MOSA/test_stack4.py.orig
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
    bool_0 = True
    linked_list_0 = module_0.LinkedList(bool_0)
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.display()
    assert var_0 == '(True)'

def test_case_2():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None

def test_case_3():
    none_type_0 = None
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    var_0 = stack_0.push(none_type_0)
    str_0 = '\\c~?T44f#\nkO+'
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_1 = linked_list_0.display()
    assert var_1 == '(+, O, k, \n, #, f, 4, 4, T, ?, ~, c, \\)'
    node_0 = module_0.Node(stack_0)
    stack_1 = module_0.Stack()
    var_2 = linked_list_0.remove(none_type_0)
    var_3 = linked_list_0.pop()
    assert var_3 == '+'

def test_case_4():
    none_type_0 = None
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    str_0 = '\\c~?T44f#\nkO+'
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.display()
    assert var_0 == '(+, O, k, \n, #, f, 4, 4, T, ?, ~, c, \\)'
    node_0 = module_0.Node(stack_0)
    var_1 = linked_list_0.remove(none_type_0)

def test_case_5():
    none_type_0 = None
    node_0 = module_0.Node(none_type_0)
    str_0 = '\\c~?T44f#\nkO+'
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.display()
    assert var_0 == '(+, O, k, \n, #, f, 4, 4, T, ?, ~, c, \\)'
    node_1 = module_0.Node(var_0)
    assert node_1.data == '(+, O, k, \n, #, f, 4, 4, T, ?, ~, c, \\)'
    linked_list_1 = module_0.LinkedList(var_0)
    assert f'{type(linked_list_1.head).__module__}.{type(linked_list_1.head).__qualname__}' == 'stack4.Node'
    var_1 = linked_list_1.remove(var_0)
    var_2 = linked_list_1.push(var_1)
    var_3 = linked_list_1.remove(node_1)
    bool_0 = False
    var_4 = linked_list_1.search(bool_0)

def test_case_6():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    bool_0 = False
    var_0 = linked_list_0.push(bool_0)
    var_1 = linked_list_0.search(bool_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'stack4.Node'
    assert var_1.data is False
    assert var_1.next is None
    linked_list_1 = module_0.LinkedList()
    assert linked_list_1.head is None
    stack_0 = module_0.Stack()

def test_case_7():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.remove(linked_list_0)
    var_1 = linked_list_0.search(linked_list_0)

def test_case_8():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.remove(linked_list_0)

def test_case_9():
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    str_0 = '\\c~?T44f#\nkO+'
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.display()
    assert var_0 == '(+, O, k, \n, #, f, 4, 4, T, ?, ~, c, \\)'
    node_0 = module_0.Node(stack_0)
    stack_1 = module_0.Stack()
    var_1 = linked_list_0.remove(var_0)

def test_case_10():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.display()
    assert var_0 == ')'

def test_case_11():
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    list_0 = [stack_0, stack_0]
    node_0 = module_0.Node(list_0)

def test_case_12():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'stack4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.remove(linked_list_0)
    var_1 = linked_list_0.size()
    assert var_1 == 0

def test_case_13():
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'

def test_case_14():
    none_type_0 = None
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    str_0 = '\\c~?T44f#\nkO+'
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.remove(none_type_0)

def test_case_15():
    none_type_0 = None
    str_0 = "4'8tA-a"
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.pop()
    assert var_0 == 'a'
    var_1 = linked_list_0.remove(str_0)
    var_2 = linked_list_0.push(var_1)
    var_3 = linked_list_0.remove(none_type_0)

def test_case_16():
    none_type_0 = None
    stack_0 = module_0.Stack()
    assert f'{type(stack_0).__module__}.{type(stack_0).__qualname__}' == 'stack4.Stack'
    stack_1 = module_0.Stack()
    float_0 = 586.5
    int_0 = 187
    tuple_0 = (int_0,)
    set_0 = {float_0, stack_1, tuple_0}
    linked_list_0 = module_0.LinkedList(set_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'stack4.Node'
    var_0 = linked_list_0.display()
    var_1 = linked_list_0.remove(float_0)
