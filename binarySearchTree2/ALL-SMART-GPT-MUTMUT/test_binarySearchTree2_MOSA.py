#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree2/MOSA/test_binarySearchTree2.py.orig
import pytest
import binarySearchTree2 as module_0

def test_case_0():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0

def test_case_1():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.add(b_s_t_0)
    assert len(b_s_t_0) == 1
    node_0 = module_0.Node(var_0)
    assert node_0.value is None
    var_1 = b_s_t_0.minValueNode(node_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'binarySearchTree2.Node'
    assert var_1.value is None
    assert var_1.left is None
    assert var_1.right is None

def test_case_2():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.__str__()
    assert var_0 == '[]'
    list_0 = [b_s_t_0]
    none_type_0 = b_s_t_0.build(list_0)
    assert len(b_s_t_0) == 1
    var_1 = b_s_t_0.__str__()
    var_2 = b_s_t_0.isValid()
    var_3 = b_s_t_0.add(b_s_t_0)
    assert var_3 is False
    var_4 = var_0.__str__()
    assert var_4 == '[]'

def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    none_type_0 = b_s_t_0.build(list_0)
    assert len(b_s_t_0) == 2

def test_case_4():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.__str__()
    assert var_0 == '[]'
    none_type_0 = b_s_t_0.build(var_0)
    assert len(b_s_t_0) == 2
    var_1 = b_s_t_0.add(var_0)
    assert len(b_s_t_0) == 3
    var_2 = b_s_t_0.remove(var_0)
    assert len(b_s_t_0) == 2
    var_3 = b_s_t_0.getOrder(var_0)

def test_case_5():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    none_type_0 = b_s_t_0.build(list_0)
    assert len(b_s_t_0) == 2

def test_case_6():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    node_0 = module_0.Node(b_s_t_0)
    assert len(node_0.value) == 0
    var_0 = b_s_t_0.minValueNode(node_0)
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree2.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'binarySearchTree2.BST'
    assert len(var_0.value) == 0
    assert var_0.left is None
    assert var_0.right is None

def test_case_7():
    float_0 = -892.881462
    tuple_0 = ()
    set_0 = {tuple_0, tuple_0}
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.remove(set_0)

def test_case_8():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    list_0 = [b_s_t_0]
    none_type_0 = b_s_t_0.build(list_0)
    assert len(b_s_t_0) == 1

def test_case_9():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    bool_0 = False
    var_0 = b_s_t_0.add(bool_0)
    assert len(b_s_t_0) == 1
    var_1 = b_s_t_0.__str__()
    assert var_1 == '[False]'
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0
    var_2 = b_s_t_0.getOrder(var_1)

def test_case_10():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.isValid()
    node_0 = module_0.Node(var_0)
    var_1 = b_s_t_0.minValueNode(node_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'binarySearchTree2.Node'
    assert var_1.value is None
    assert var_1.left is None
    assert var_1.right is None

def test_case_11():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    none_type_0 = b_s_t_0.build(list_0)
    assert len(b_s_t_0) == 3
    var_0 = b_s_t_0.__len__()
    assert var_0 == 3

def test_case_12():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    var_0 = b_s_t_0.__str__()
    assert var_0 == '[]'
    var_1 = b_s_t_0.add(var_0)
    assert len(b_s_t_0) == 1
    node_0 = module_0.Node(var_0)
    assert node_0.value == '[]'
    var_2 = b_s_t_0.minValueNode(node_0)
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'binarySearchTree2.Node'
    assert var_2.value == '[]'
    assert var_2.left is None
    assert var_2.right is None
    var_3 = b_s_t_0.remove(var_0)
    assert len(b_s_t_0) == 0
    var_4 = b_s_t_0.getOrder(var_0)

def test_case_13():
    float_0 = 692.3135980143779
    bool_0 = True
    list_0 = [float_0, bool_0, bool_0, float_0]
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    none_type_0 = b_s_t_0.build(list_0)
    assert len(b_s_t_0) == 4

def test_case_14():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    none_type_0 = b_s_t_0.build(list_0)
    assert len(b_s_t_0) == 4

def test_case_15():
    b_s_t_0 = module_0.BST()
    assert len(b_s_t_0) == 0
    bool_0 = False
    var_0 = b_s_t_0.add(bool_0)
    assert len(b_s_t_0) == 1
    var_1 = b_s_t_0.__str__()
    assert var_1 == '[False]'
    none_type_0 = b_s_t_0.build(var_1)
    assert len(b_s_t_0) == 8
    b_s_t_1 = module_0.BST()
    assert len(b_s_t_1) == 0
    var_2 = b_s_t_0.getOrder(var_1)
