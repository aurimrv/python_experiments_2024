#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree4/MOSA/test_binarySearchTree4.py.orig
import pytest
import binarySearchTree4 as module_0
import builtins as module_1

def test_case_0():
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

def test_case_1():
    bytes_0 = b'!\xaa\x8f/U\xbe\xaa\x87\xf5\xfdw'
    object_0 = module_1.object()
    bst_0 = module_0.Bst(object_0)

def test_case_2():
    none_type_0 = None
    bst_0 = module_0.Bst()
    with pytest.raises(TypeError):
        bst_0.insert(none_type_0)

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
    var_0 = bst_0.insert(bool_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data is False
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    int_0 = -1820
    node_0 = module_0.Node(int_0)
    var_1 = var_0.__repr__()
    node_1 = module_0.Node(node_0)
    var_2 = node_1.__repr__()
    var_3 = var_2.__repr__()
    bool_1 = False
    var_4 = bst_0.insert(bool_1)
    assert f'{type(var_0.left).__module__}.{type(var_0.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_4.parent).__module__}.{type(var_4.parent).__qualname__}' == 'binarySearchTree4.Node'
    object_0 = module_1.object()
    bst_1 = module_0.Bst()
    bool_2 = True
    var_5 = bst_0.insert(bool_2)
    assert f'{type(var_0.right).__module__}.{type(var_0.right).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_5.parent).__module__}.{type(var_5.parent).__qualname__}' == 'binarySearchTree4.Node'
    var_6 = node_1.__repr__()
    with pytest.raises(TypeError):
        bst_0.insert(var_4)

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
    node_0 = module_0.Node(var_0)
    node_1 = module_0.Node(node_0)
    var_1 = module_0.Node(node_0)
    bool_1 = False
    var_2 = bst_0.insert(bool_1)
    assert f'{type(var_0.left).__module__}.{type(var_0.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_2.parent).__module__}.{type(var_2.parent).__qualname__}' == 'binarySearchTree4.Node'
    object_0 = module_1.object()
    bool_2 = True
    var_3 = bst_0.insert(bool_2)
    assert f'{type(var_2.right).__module__}.{type(var_2.right).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_3.parent).__module__}.{type(var_3.parent).__qualname__}' == 'binarySearchTree4.Node'
    var_4 = var_0.__repr__()

def test_case_8():
    bst_0 = module_0.Bst()
    int_0 = -1820
    node_0 = module_0.Node(int_0)
    var_0 = bst_0.insert(int_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data == -1820
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    bool_0 = False
    var_1 = bst_0.insert(bool_0)
    assert f'{type(var_0.right).__module__}.{type(var_0.right).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_1.parent).__module__}.{type(var_1.parent).__qualname__}' == 'binarySearchTree4.Node'
    object_0 = module_1.object()
    bst_1 = module_0.Bst()
    bool_1 = True
    var_2 = bst_0.insert(bool_1)
    assert f'{type(var_1.right).__module__}.{type(var_1.right).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_2.parent).__module__}.{type(var_2.parent).__qualname__}' == 'binarySearchTree4.Node'
    with pytest.raises(TypeError):
        bst_0.insert(var_1)
