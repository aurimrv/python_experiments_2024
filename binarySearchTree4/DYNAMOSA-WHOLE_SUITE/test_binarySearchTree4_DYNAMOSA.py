#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree4/DYNAMOSA/test_binarySearchTree4.py.orig
import pytest
import binarySearchTree4 as module_0

def test_case_0():
    none_type_0 = None
    bst_0 = module_0.Bst()
    with pytest.raises(TypeError):
        bst_0.insert(none_type_0)

def test_case_1():
    none_type_0 = None
    node_0 = module_0.Node(none_type_0)
    bst_0 = module_0.Bst()
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'binarySearchTree4.Bst'
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None

def test_case_2():
    bst_0 = module_0.Bst()
    str_0 = 'Eq$Iy6fg;+)U <2SrvUq'
    var_0 = bst_0.insert(str_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data == 'Eq$Iy6fg;+)U <2SrvUq'
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    with pytest.raises(TypeError):
        bst_0.insert(var_0)

def test_case_3():
    int_0 = -5052
    node_0 = module_0.Node(int_0)

def test_case_4():
    bst_0 = module_0.Bst()
    str_0 = 'Eq$Iy6fg;+)U <2SrvUq'
    var_0 = bst_0.insert(str_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data == 'Eq$Iy6fg;+)U <2SrvUq'
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    var_1 = var_0.__repr__()

def test_case_5():
    tuple_0 = ()
    node_0 = module_0.Node(tuple_0)
    bst_0 = module_0.Bst()

def test_case_6():
    bool_0 = False
    bst_0 = module_0.Bst()
    bst_1 = module_0.Bst(bst_0)
    var_0 = bst_0.insert(bool_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data is False
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    node_0 = module_0.Node(bool_0)
    bst_2 = module_0.Bst()
    bool_1 = True
    var_1 = bst_0.insert(bool_1)
    assert f'{type(var_0.right).__module__}.{type(var_0.right).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_1.parent).__module__}.{type(var_1.parent).__qualname__}' == 'binarySearchTree4.Node'

def test_case_7():
    bool_0 = False
    node_0 = module_0.Node(bool_0)
    var_0 = node_0.__repr__()
    bst_0 = module_0.Bst()
    var_1 = bst_0.insert(bool_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'binarySearchTree4.Node'
    assert var_1.data is False
    assert var_1.left is None
    assert var_1.right is None
    assert var_1.parent is None
    var_2 = bst_0.insert(bool_0)
    assert f'{type(var_1.left).__module__}.{type(var_1.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_2.parent).__module__}.{type(var_2.parent).__qualname__}' == 'binarySearchTree4.Node'
    var_3 = var_1.__repr__()
    str_0 = 'fRiH'
    bytes_0 = b'\x99'
    node_1 = module_0.Node(bytes_0)
    var_4 = node_1.__repr__()
    var_5 = var_3.__repr__()
    var_6 = var_1.__repr__()
    node_2 = module_0.Node(var_6)

def test_case_8():
    tuple_0 = ()
    bst_0 = module_0.Bst()
    var_0 = bst_0.insert(tuple_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data == ()
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    var_1 = bst_0.insert(tuple_0)
    assert f'{type(var_0.left).__module__}.{type(var_0.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_1.parent).__module__}.{type(var_1.parent).__qualname__}' == 'binarySearchTree4.Node'
    var_2 = var_1.__repr__()
    var_3 = var_2.__repr__()
    var_4 = bst_0.insert(tuple_0)
    assert f'{type(var_1.left).__module__}.{type(var_1.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_4.parent).__module__}.{type(var_4.parent).__qualname__}' == 'binarySearchTree4.Node'
    node_0 = module_0.Node(var_1)
    var_5 = var_4.__repr__()

def test_case_9():
    bool_0 = False
    int_0 = -2088
    bst_0 = module_0.Bst()
    var_0 = bst_0.insert(int_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data == -2088
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    bst_1 = module_0.Bst()
    float_0 = 3874.2
    var_1 = bst_0.insert(float_0)
    assert f'{type(var_0.right).__module__}.{type(var_0.right).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_1.parent).__module__}.{type(var_1.parent).__qualname__}' == 'binarySearchTree4.Node'
    var_2 = bst_1.insert(var_0)
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'binarySearchTree4.Node'
    var_3 = var_1.__repr__()
    str_0 = 'fRiH'
    node_0 = module_0.Node(bool_0)
    var_4 = var_0.__repr__()
    node_1 = module_0.Node(var_0)
    node_2 = module_0.Node(str_0)
    var_5 = bst_0.insert(bool_0)
    assert f'{type(var_1.left).__module__}.{type(var_1.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_5.parent).__module__}.{type(var_5.parent).__qualname__}' == 'binarySearchTree4.Node'
    var_6 = var_5.__repr__()
    bst_2 = module_0.Bst()
