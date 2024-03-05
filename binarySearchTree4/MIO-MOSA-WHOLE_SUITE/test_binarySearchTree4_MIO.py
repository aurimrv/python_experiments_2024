#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree4/MIO/test_binarySearchTree4.py.orig
import pytest
import binarySearchTree4 as module_0

def test_case_0():
    bst_0 = module_0.Bst()
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'binarySearchTree4.Bst'
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None

def test_case_1():
    bst_0 = module_0.Bst()
    var_0 = bst_0.insert(bst_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'binarySearchTree4.Bst'
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    with pytest.raises(TypeError):
        bst_0.insert(var_0)

def test_case_2():
    bst_0 = module_0.Bst()
    none_type_0 = None
    with pytest.raises(TypeError):
        bst_0.insert(none_type_0)

def test_case_3():
    bytes_0 = b'\xca\x89@KfH\xa7\xf9\x08\xd5S!\xb5\xb2\xb4\xee\n\x04\xe8'
    bst_0 = module_0.Bst()
    var_0 = bst_0.insert(bytes_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data == b'\xca\x89@KfH\xa7\xf9\x08\xd5S!\xb5\xb2\xb4\xee\n\x04\xe8'
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    var_1 = bst_0.insert(bytes_0)
    assert f'{type(var_0.left).__module__}.{type(var_0.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_1.parent).__module__}.{type(var_1.parent).__qualname__}' == 'binarySearchTree4.Node'

def test_case_4():
    bytes_0 = b'\xca\x89@KfH\xa7\xf9\x08\xd5S!\xb5\xb2\xb4\xee\n\x04\xe8'
    bst_0 = module_0.Bst()
    bytes_1 = b'I\x1e\x9a\xbc\xbc\x83\xbbg\x9d\x89\xfe\x02\x9c\n'
    var_0 = bst_0.insert(bytes_1)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data == b'I\x1e\x9a\xbc\xbc\x83\xbbg\x9d\x89\xfe\x02\x9c\n'
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    var_1 = bst_0.insert(bytes_0)
    assert f'{type(var_0.right).__module__}.{type(var_0.right).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_1.parent).__module__}.{type(var_1.parent).__qualname__}' == 'binarySearchTree4.Node'

def test_case_5():
    bytes_0 = b'\xca\x89@KfH\xd1\xa7\xf9\x08\xd5S!\xb5\xb2\xb4\xe6\n\xd2\xa8'
    none_type_0 = None
    node_0 = module_0.Node(none_type_0)
    bst_0 = module_0.Bst()
    var_0 = bst_0.insert(bytes_0)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data == b'\xca\x89@KfH\xd1\xa7\xf9\x08\xd5S!\xb5\xb2\xb4\xe6\n\xd2\xa8'
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    bst_1 = module_0.Bst()
    bst_2 = module_0.Bst()
    bytes_1 = b'+ "\xdf\xa2zG\x85\xd6T'
    bool_0 = True
    var_1 = bst_1.insert(bytes_1)
    assert f'{type(bst_1.root).__module__}.{type(bst_1.root).__qualname__}' == 'binarySearchTree4.Node'
    var_2 = bst_1.insert(bytes_0)
    assert f'{type(var_1.right).__module__}.{type(var_1.right).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_2.parent).__module__}.{type(var_2.parent).__qualname__}' == 'binarySearchTree4.Node'
    var_3 = bst_1.insert(bytes_0)
    assert f'{type(var_2.left).__module__}.{type(var_2.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_3.parent).__module__}.{type(var_3.parent).__qualname__}' == 'binarySearchTree4.Node'

def test_case_6():
    bytes_0 = b'\xca\x89@KfH\xa7\xf9\x08\xd5S!\xb5\xb2\xb4\xee\n\x04\xe8'
    bst_0 = module_0.Bst()
    bytes_1 = b'\xe8\xcb\x12\xab!\x04\xdeu\x9bY\x1c\xbc\x89\xf5\xba\xa1\xf4\xf3_1'
    var_0 = bst_0.insert(bytes_1)
    assert f'{type(bst_0.root).__module__}.{type(bst_0.root).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree4.Node'
    assert var_0.data == b'\xe8\xcb\x12\xab!\x04\xdeu\x9bY\x1c\xbc\x89\xf5\xba\xa1\xf4\xf3_1'
    assert var_0.left is None
    assert var_0.right is None
    assert var_0.parent is None
    var_1 = bst_0.insert(bytes_0)
    assert f'{type(var_0.left).__module__}.{type(var_0.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_1.parent).__module__}.{type(var_1.parent).__qualname__}' == 'binarySearchTree4.Node'
    var_2 = bst_0.insert(bytes_0)
    assert f'{type(var_1.left).__module__}.{type(var_1.left).__qualname__}' == 'binarySearchTree4.Node'
    assert f'{type(var_2.parent).__module__}.{type(var_2.parent).__qualname__}' == 'binarySearchTree4.Node'

def test_case_7():
    bst_0 = module_0.Bst()

def test_case_8():
    set_0 = set()
    node_0 = module_0.Node(set_0)

def test_case_9():
    bst_0 = module_0.Bst()
    node_0 = module_0.Node(bst_0)
    var_0 = node_0.__repr__()
