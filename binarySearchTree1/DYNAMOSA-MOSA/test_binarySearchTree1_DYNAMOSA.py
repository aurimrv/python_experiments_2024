#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/binarySearchTree1/DYNAMOSA/test_binarySearchTree1.py.orig
import pytest
import binarySearchTree1 as module_0
import builtins as module_1

def test_case_0():
    int_0 = 442
    binary_node_0 = module_0.BinaryNode(int_0)
    var_0 = binary_node_0.add(int_0)
    assert f'{type(binary_node_0.left).__module__}.{type(binary_node_0.left).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_1():
    none_type_0 = None
    binary_node_0 = module_0.BinaryNode(none_type_0)
    var_0 = binary_node_0.__repr__()
    assert var_0 == '(L: None R:)'

def test_case_2():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.remove(binary_tree_0)
    var_1 = binary_tree_0.__contains__(var_0)
    assert var_1 is False
    var_2 = binary_tree_0.add(var_1)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.add(var_1)
    var_4 = binary_tree_0.remove(var_1)

def test_case_3():
    none_type_0 = None
    binary_node_0 = module_0.BinaryNode(none_type_0)
    var_0 = binary_node_0.__repr__()
    assert var_0 == '(L: None R:)'

def test_case_4():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_1 = binary_tree_0.getMin()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'binarySearchTree1.BinaryTree'
    assert f'{type(var_1.root).__module__}.{type(var_1.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.__iter__()

def test_case_5():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.remove(binary_tree_0)
    with pytest.raises(ValueError):
        binary_tree_0.getMin()

def test_case_6():
    binary_tree_0 = module_0.BinaryTree()
    with pytest.raises(ValueError):
        binary_tree_0.getMax()

def test_case_7():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(binary_tree_0)
    var_1 = binary_tree_0.__contains__(binary_tree_0)
    assert var_1 is False

def test_case_8():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__iter__()
    var_1 = binary_tree_0.__repr__()
    assert var_1 == 'binary:()'
    var_2 = binary_tree_0.add(var_1)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_9():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.remove(binary_tree_0)
    var_1 = binary_tree_0.__contains__(var_0)
    assert var_1 is False
    var_2 = binary_tree_0.add(var_1)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.add(var_1)
    var_4 = binary_tree_0.__repr__()
    assert var_4 == 'binary:(L:(L: False R:) False R:)'
    var_5 = binary_tree_0.remove(var_1)

def test_case_10():
    binary_tree_0 = module_0.BinaryTree()

def test_case_11():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    binary_node_0 = module_0.BinaryNode(list_0)
    var_0 = binary_node_0.remove(list_0)

def test_case_12():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.getMax()
    assert var_2 is False
    var_3 = binary_tree_0.closest(var_2)
    assert var_3 is False

def test_case_13():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.getMax()
    assert var_2 is False
    var_3 = binary_tree_0.__contains__(var_2)
    assert var_3 is True
    var_4 = binary_tree_0.closest(var_2)
    assert var_4 is False
    var_5 = var_2.__repr__()
    var_6 = binary_tree_0.remove(var_3)

def test_case_14():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.getMax()
    assert var_2 is False
    var_3 = binary_tree_0.__contains__(var_2)
    assert var_3 is True
    var_4 = var_2.__repr__()

def test_case_15():
    binary_tree_0 = module_0.BinaryTree()
    none_type_0 = None
    var_0 = binary_tree_0.__iter__()
    binary_node_0 = module_0.BinaryNode(none_type_0)
    object_0 = module_1.object(*var_0)
    var_1 = module_0.BinaryTree()

def test_case_16():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.remove(binary_tree_0)
    var_1 = binary_tree_0.__contains__(var_0)
    assert var_1 is False
    var_2 = binary_tree_0.add(var_1)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = var_1.__repr__()
    var_4 = binary_tree_0.getMin()
    assert var_4 is False
    var_5 = binary_tree_0.getMax()
    assert var_5 is False
    var_6 = binary_tree_0.__contains__(var_5)
    assert var_6 is True
    int_0 = 451
    var_7 = binary_tree_0.closest(int_0)
    assert var_7 is False
    var_8 = var_2.__repr__()
    var_9 = binary_tree_0.__repr__()
    assert var_9 == 'binary:(L: False R:)'
    var_10 = binary_tree_0.add(int_0)
    var_11 = binary_tree_0.remove(var_6)

def test_case_17():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.__contains__(var_0)
    assert var_2 is True
    var_3 = binary_tree_0.getMax()
    assert var_3 is False
    var_4 = var_1.__repr__()
    var_5 = binary_tree_0.__contains__(var_2)
    assert var_5 is False
    var_6 = binary_tree_0.add(var_5)
    var_7 = binary_tree_0.remove(var_3)
    var_8 = binary_tree_0.__repr__()
    assert var_8 == 'binary:(L: False R:)'
    binary_node_0 = module_0.BinaryNode(var_8)
    assert binary_node_0.value == 'binary:(L: False R:)'

def test_case_18():
    bool_0 = True
    bool_1 = False
    binary_node_0 = module_0.BinaryNode(bool_1)
    var_0 = binary_node_0.add(bool_0)
    assert f'{type(binary_node_0.right).__module__}.{type(binary_node_0.right).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_19():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(binary_tree_0)
    var_1 = binary_tree_0.__contains__(var_0)
    assert var_1 is False
    var_2 = binary_tree_0.add(var_1)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.__contains__(var_1)
    assert var_3 is True
    var_4 = binary_tree_0.add(var_3)
    var_5 = binary_tree_0.getMax()
    assert var_5 is True
    var_6 = binary_tree_0.add(var_5)
    var_7 = binary_tree_0.remove(var_1)
    binary_node_0 = module_0.BinaryNode(var_6)
    var_8 = binary_tree_0.__iter__()
    var_9 = binary_tree_0.remove(var_1)

def test_case_20():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(binary_tree_0)
    var_1 = binary_tree_0.__contains__(var_0)
    assert var_1 is False
    var_2 = binary_tree_0.add(var_1)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.__contains__(var_1)
    assert var_3 is True
    var_4 = binary_tree_0.add(var_3)
    var_5 = binary_tree_0.getMax()
    assert var_5 is True
    var_6 = binary_tree_0.add(var_5)
    binary_node_0 = module_0.BinaryNode(var_6)
    var_7 = binary_tree_0.__iter__()

def test_case_21():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.remove(binary_tree_0)
    var_2 = binary_tree_0.__contains__(var_1)
    var_3 = binary_tree_0.add(var_2)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_4 = binary_tree_0.getMin()
    assert var_4 is False
    var_5 = binary_tree_0.getMax()
    assert var_5 is False
    binary_tree_1 = module_0.BinaryTree()
    var_6 = binary_tree_0.__contains__(var_5)
    assert var_6 is True
    int_0 = -201
    var_7 = binary_tree_0.closest(int_0)
    assert var_7 is False

def test_case_22():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(binary_tree_0)
    var_1 = binary_tree_0.__contains__(var_0)
    assert var_1 is False
    var_2 = binary_tree_0.add(var_1)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.__contains__(var_1)
    assert var_3 is True
    var_4 = binary_tree_0.add(var_3)
    var_5 = binary_tree_0.getMax()
    assert var_5 is True
    var_6 = binary_tree_0.closest(var_5)
    assert var_6 is True
    var_7 = var_2.__repr__()
    var_8 = binary_tree_0.add(var_6)
    var_9 = binary_tree_0.__repr__()
    assert var_9 == 'binary:(L: False R:(L:(L: True R:) True R:))'
    binary_node_0 = module_0.BinaryNode(var_8)
    var_10 = binary_node_0.__repr__()
    assert var_10 == '(L: None R:)'

def test_case_23():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(binary_tree_0)
    var_1 = binary_tree_0.__contains__(var_0)
    assert var_1 is False
    var_2 = binary_tree_0.add(var_1)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.__contains__(var_1)
    assert var_3 is True
    var_4 = binary_tree_0.add(var_3)
    var_5 = binary_tree_0.getMax()
    assert var_5 is True
    var_6 = binary_tree_0.closest(var_5)
    assert var_6 is True
    var_7 = var_2.__repr__()
    var_8 = binary_tree_0.add(var_6)
    var_9 = binary_tree_0.remove(var_6)
    binary_node_0 = module_0.BinaryNode(var_8)
    var_10 = binary_tree_0.add(var_3)

def test_case_24():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.remove(binary_tree_0)
    var_1 = binary_tree_0.__contains__(var_0)
    assert var_1 is False
    var_2 = binary_tree_0.add(var_1)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.add(var_1)
    var_4 = binary_tree_0.getMax()
    assert var_4 is False
    var_5 = var_3.__repr__()
    var_6 = binary_tree_0.__repr__()
    assert var_6 == 'binary:(L:(L: False R:) False R:)'
    binary_node_0 = module_0.BinaryNode(var_5)
    var_7 = binary_tree_0.getMin()
    assert var_7 is False
    var_8 = binary_tree_0.remove(var_4)

def test_case_25():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.__contains__(binary_tree_0)
    assert var_0 is False
    var_1 = binary_tree_0.add(var_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_2 = binary_tree_0.add(var_0)
    var_3 = binary_tree_0.getMin()
    assert var_3 is False
    var_4 = binary_tree_0.getMax()
    assert var_4 is False
    var_5 = var_2.__repr__()
    binary_node_0 = module_0.BinaryNode(var_5)
    var_6 = binary_tree_0.add(var_0)
    var_7 = binary_tree_0.getMin()
    var_8 = binary_tree_0.remove(var_7)

def test_case_26():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(binary_tree_0)
    var_1 = binary_tree_0.add(binary_tree_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'

def test_case_27():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(binary_tree_0)
    var_1 = binary_tree_0.__contains__(var_0)
    assert var_1 is False
    var_2 = binary_tree_0.add(var_1)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.__contains__(var_1)
    assert var_3 is True
    var_4 = binary_tree_0.add(var_3)
    var_5 = binary_tree_0.getMax()
    assert var_5 is True
    var_6 = var_5.__repr__()
    assert var_6 == 'True'
    var_7 = binary_tree_0.__contains__(var_3)
    assert var_7 is True

def test_case_28():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(binary_tree_0)
    var_1 = binary_tree_0.__contains__(var_0)
    assert var_1 is False
    int_0 = 3380
    var_2 = binary_tree_0.add(int_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.add(var_1)
    var_4 = binary_tree_0.__contains__(var_1)
    assert var_4 is True
    var_5 = binary_tree_0.add(var_4)
    var_6 = binary_tree_0.getMax()
    assert var_6 == 3380
    var_7 = binary_tree_0.closest(var_6)
    var_8 = var_3.__repr__()
    var_9 = binary_tree_0.add(var_7)
    var_10 = binary_tree_0.remove(var_7)
    var_11 = binary_tree_0.__repr__()
    assert var_11 == 'binary:(L:(L: False R:(L: True R:)) 3380 R:)'
    binary_node_0 = module_0.BinaryNode(var_9)

def test_case_29():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(binary_tree_0)
    var_1 = binary_tree_0.__contains__(var_0)
    assert var_1 is False
    var_2 = binary_tree_0.add(var_1)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.__contains__(var_1)
    assert var_3 is True
    var_4 = binary_tree_0.add(var_3)
    var_5 = binary_tree_0.getMax()
    assert var_5 is True
    var_6 = binary_tree_0.closest(var_5)
    assert var_6 is True
    var_7 = var_2.__repr__()
    var_8 = binary_tree_0.add(var_6)

def test_case_30():
    binary_tree_0 = module_0.BinaryTree()
    var_0 = binary_tree_0.closest(binary_tree_0)
    var_1 = binary_tree_0.__contains__(var_0)
    assert var_1 is False
    int_0 = -4493
    var_2 = binary_tree_0.add(int_0)
    assert f'{type(binary_tree_0.root).__module__}.{type(binary_tree_0.root).__qualname__}' == 'binarySearchTree1.BinaryNode'
    var_3 = binary_tree_0.add(var_1)
    var_4 = binary_tree_0.__contains__(var_1)
    assert var_4 is True
    var_5 = binary_tree_0.add(var_4)
    var_6 = binary_tree_0.getMax()
    assert var_6 is True
    var_7 = binary_tree_0.closest(var_6)
    assert var_7 is True
    var_8 = var_3.__repr__()
    var_9 = binary_tree_0.add(var_7)
    var_10 = module_1.object()
    var_11 = binary_tree_0.__repr__()
    assert var_11 == 'binary:(L: -4493 R:(L: False R:(L:(L: True R:) True R:)))'
    binary_node_0 = module_0.BinaryNode(var_9)
