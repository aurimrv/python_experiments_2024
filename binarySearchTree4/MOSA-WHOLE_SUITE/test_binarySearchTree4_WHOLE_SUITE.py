#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree4/WHOLE_SUITE/test_binarySearchTree4.py.orig
import pytest
import binarySearchTree4 as module_0

def test_case_0():
    bst_0 = module_0.Bst()
    bst_1 = module_0.Bst()
    bst_2 = module_0.Bst()
    bst_3 = module_0.Bst()
    bool_0 = False
    int_0 = 1568
    list_0 = [int_0]
    complex_0 = -46.48 + 1184.7075j
    var_0 = bst_0.insert(list_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data == [1568]
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    node_0 = module_0.Node(complex_0)
    complex_1 = 982.226 + 1493.681249j
    var_1 = bst_3.insert(bool_0)
    assert f'{type(bst_3.root).__module__}.{type(bst_3.root).__qualname__}' == 'binarySearchTree4.Node'
    float_0 = 1099.91
    tuple_0 = (complex_1, float_0)
    none_type_0 = None
    node_1 = module_0.Node(tuple_0)
    var_2 = node_1.__repr__()
    var_3 = bst_3.insert(float_0)
    assert f'{type(var_1.right).__module__}.{type(var_1.right).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_3.parent).__module__}.{type(var_3.parent).__qualname__}' == 'binarySearchTree4.Node'
    node_2 = module_0.Node(none_type_0)
    node_3 = bst_3.insert(float_0)
    assert f'{type(var_3.left).__module__}.{type(var_3.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(node_3.parent).__module__}.{type(node_3.parent).__qualname__}' == 'binarySearchTree4.Node'
    var_4 = node_2.__repr__()
    node_4 = module_0.Node(complex_0)

def test_case_1():
    bool_0 = False
    tuple_0 = (bool_0,)
    bool_1 = True
    node_0 = module_0.Node(bool_1)
    node_1 = module_0.Node(node_0)
    node_2 = module_0.Node(bool_0)
    bst_0 = module_0.Bst()
    node_3 = module_0.Node(bool_1)
    var_0 = node_0.__repr__()
    var_1 = node_2.__repr__()
    var_2 = var_1.__repr__()

def test_case_2():
    bool_0 = True
    none_type_0 = None
    node_0 = module_0.Node(none_type_0)
    var_0 = node_0.__repr__()
    var_1 = node_0.__repr__()

def test_case_3():
    bool_0 = True
    none_type_0 = None
    node_0 = module_0.Node(none_type_0)
    var_0 = node_0.__repr__()
    var_1 = node_0.__repr__()

def test_case_4():
    none_type_0 = None
    bst_0 = module_0.Bst()
    with pytest.raises(TypeError):
        bst_0.insert(none_type_0)

def test_case_5():
    none_type_0 = None
    bst_0 = module_0.Bst()
    with pytest.raises(TypeError):
        bst_0.insert(none_type_0)

def test_case_6():
    bst_0 = module_0.Bst()
    int_0 = -852
    bst_1 = module_0.Bst()
    var_0 = bst_1.insert(int_0)
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data == -852
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    var_1 = bst_0.__repr__()
    with pytest.raises(TypeError):
        bst_1.insert(var_1)

def test_case_7():
    bool_0 = True
    bst_0 = module_0.Bst()
    var_0 = bst_0.insert(bool_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data is True
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    var_1 = bst_0.insert(bool_0)
    assert f'{type(var_0.left).__module__}.{type(var_0.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_1.parent).__module__}.{type(var_1.parent).__qualname__}' == 'binarySearchTree4.Node'
    var_2 = bst_0.insert(bool_0)
    assert f'{type(var_1.left).__module__}.{type(var_1.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_2.parent).__module__}.{type(var_2.parent).__qualname__}' == 'binarySearchTree4.Node'
    var_3 = var_2.__repr__()
    var_4 = var_3.__repr__()
    var_5 = var_4.__repr__()
    var_6 = var_5.__repr__()
    var_7 = var_6.__repr__()

def test_case_8():
    int_0 = -330
    set_0 = {int_0, int_0, int_0, int_0}
    bst_0 = module_0.Bst(set_0)
