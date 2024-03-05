#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree1/WHOLE_SUITE/test_binarySearchTree1.py.orig
import pytest
import binarySearchTree1 as module_0
import builtins as module_1

def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__iter__()
    binary_node_0 = module_0.BinaryNode(list_0)
    binary_tree_1 = module_0.BinaryTree()
    binary_tree_2 = module_0.BinaryTree()
    var_1 = binary_tree_2.__repr__()
    assert var_1 == 'binary:()'
    with pytest.raises(ValueError):
        binary_tree_1.getMin()

def test_case_1():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_2():
    list_0 = []
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(list_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = binary_tree_0.add(list_0)
    var_2 = binary_tree_0.add(list_0)
    var_3 = binary_tree_0.getMin()
    binary_node_0 = module_0.BinaryNode(var_2)
    var_4 = binary_tree_0.__contains__(list_0)
    assert var_4 is True
    var_5 = binary_tree_0.getMin()

def test_case_3():
    binary_tree_0 = module_0.BinaryTree()
    float_0 = -1660.53234
    str_0 = 'BhpUfU<<C<'
    var_0 = binary_tree_0.remove(float_0)
    var_1 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.getMax()
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_2.root).__module__}.{type(var_2.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_4():
    binary_tree_0 = module_0.BinaryTree()

def test_case_5():
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(bool_0)
    var_0 = binary_node_0.removeFromParent(binary_node_0, bool_0)
    var_1 = binary_node_0.add(bool_0)
    assert f'{type(binary_node_0.left).__module__}.{type(binary_node_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_node_0.__repr__()
    assert var_2 == '(L:(L: True R:) True R:)'
    var_3 = binary_node_0.inorder()
    var_4 = binary_node_0.remove(bool_0)
    assert binary_node_0.left is None
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_4.value is True
    assert var_4.left is None
    assert var_4.right is None

def test_case_6():
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(bool_0)
    var_0 = binary_node_0.removeFromParent(binary_node_0, bool_0)
    var_1 = binary_node_0.add(bool_0)
    assert f'{type(binary_node_0.left).__module__}.{type(binary_node_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_node_0.remove(bool_0)
    assert binary_node_0.left is None
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_2.value is True
    assert var_2.left is None
    assert var_2.right is None

def test_case_7():
    bool_0 = False
    binary_node_0 = module_0.BinaryNode(bool_0)

def test_case_8():
    binary_tree_0 = module_0.BinaryTree()
    binary_tree_1 = module_0.BinaryTree()

def test_case_9():
    bytes_0 = b'<N\n'
    bool_0 = False
    none_type_0 = None
    binary_node_0 = module_0.BinaryNode(bool_0)
    var_0 = binary_node_0.__repr__()
    assert var_0 == '(L: False R:)'
    var_1 = var_0.__repr__()
    assert var_1 == "'(L: False R:)'"

def test_case_10():
    bytes_0 = b'\xd5\x1aDT\x1bg\xd27\xd3\\\x13\xba'
    set_0 = {bytes_0, bytes_0, bytes_0}
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(set_0)

def test_case_11():
    binary_tree_0 = module_0.BinaryTree()
    with pytest.raises(ValueError):
        binary_tree_0.getMin()

def test_case_12():
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(bool_0)
    bool_1 = False
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_node_0.remove(bool_1)
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_0.value is True
    assert var_0.left is None
    assert var_0.right is None
    var_1 = binary_node_0.inorder()
    binary_tree_1 = module_0.BinaryTree()
    with pytest.raises(ValueError):
        binary_tree_1.getMax()

def test_case_13():
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(bool_0)
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    none_type_0 = None
    bool_1 = False
    var_1 = binary_tree_0.__contains__(bool_1)
    assert var_1 is False
    bool_2 = False
    set_0 = {bool_2}
    var_2 = binary_tree_0.getMax()
    assert var_2 is True
    var_3 = binary_tree_0.closest(bool_2)
    assert var_3 is True
    binary_tree_1 = module_0.BinaryTree()
    object_0 = module_1.object(*binary_tree_1)

def test_case_14():
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(bool_0)
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    none_type_0 = None
    bool_1 = False
    var_1 = binary_tree_0.__contains__(bool_1)
    assert var_1 is False
    bool_2 = False
    set_0 = {bool_2}
    var_2 = binary_tree_0.getMax()
    assert var_2 is True
    var_3 = binary_tree_0.closest(bool_2)
    assert var_3 is True
    binary_tree_1 = module_0.BinaryTree()
    object_0 = module_1.object(*binary_tree_1)

def test_case_15():
    bool_0 = True
    binary_node_0 = module_0.BinaryNode(bool_0)
    bool_1 = True
    var_0 = binary_node_0.addToSubTree(binary_node_0, bool_0)
    assert f'{type(binary_node_0.left).__module__}.{type(binary_node_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert f'{type(var_0.left).__module__}.{type(var_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'
    binary_tree_0 = module_0.BinaryTree()
    var_1 = binary_tree_0.add(bool_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.add(bool_0)
    var_3 = binary_tree_0.closest(bool_1)
    assert var_3 is True
    bool_2 = False
    var_4 = binary_tree_0.getMax()
    assert var_4 is True
    var_5 = binary_tree_0.closest(bool_2)
    assert var_5 is True
    binary_tree_1 = module_0.BinaryTree()
    var_6 = binary_node_0.__repr__()
    assert var_6 == '(L:(L: True R:) True R:)'

def test_case_16():
    binary_tree_0 = module_0.BinaryTree()

def test_case_17():
    binary_tree_0 = module_0.BinaryTree()
    none_type_0 = None

def test_case_18():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.__contains__(var_0)
    assert var_2 is True
    binary_node_0 = module_0.BinaryNode(var_0)
    var_3 = binary_tree_0.getMin()
    assert var_3 is False
    var_4 = binary_tree_0.closest(var_2)
    assert var_4 is False

def test_case_19():
    bool_0 = False
    int_0 = -995
    binary_node_0 = module_0.BinaryNode(int_0)
    var_0 = binary_node_0.add(bool_0)
    assert f'{type(binary_node_0.right).__module__}.{type(binary_node_0.right).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_20():
    bool_0 = True
    bool_1 = False
    binary_node_0 = module_0.BinaryNode(bool_1)
    var_0 = binary_node_0.add(bool_0)
    assert f'{type(binary_node_0.right).__module__}.{type(binary_node_0.right).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = binary_node_0.__repr__()
    assert var_1 == '(L: False R:(L: True R:))'

def test_case_21():
    int_0 = 2683
    float_0 = 112.342
    binary_node_0 = module_0.BinaryNode(float_0)
    var_0 = binary_node_0.remove(int_0)
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'binarySearchTree1.BinaryNode'
    assert var_0.value == pytest.approx(112.342, abs=0.01, rel=0.01)
    assert var_0.left is None
    assert var_0.right is None
