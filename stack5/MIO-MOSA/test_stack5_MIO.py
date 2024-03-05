#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/stack5/MIO/test_stack5.py
import pytest
import stack5 as module_0

def test_case_0():
    stack_0 = module_0.Stack()
    var_0 = stack_0.pop()
    var_1 = stack_0.is_empty()
    var_2 = stack_0.pop()
#    var_1.push(stack_0)

def test_case_1():
    tuple_0 = ()
    dict_0 = {}
    stack_0 = module_0.Stack(dict_0)
    node_0 = module_0.Node(tuple_0)

def test_case_2():
    bool_0 = True
    stack_0 = module_0.Stack(bool_0)

def test_case_3():
    stack_0 = module_0.Stack()
    var_0 = stack_0.is_empty()

def test_case_4():
    str_0 = 'Q&!\n/.ZZ$U}~ L<d|]'
    node_0 = module_0.Node(str_0)

def test_case_5():
    int_0 = -359
    node_0 = module_0.Node(int_0)
    stack_0 = module_0.Stack()
    var_0 = stack_0.push(stack_0)
