import pytest
from binarySearchTree1 import BinaryNode, BinaryTree

def test_add():
    tree = BinaryTree()
    tree.add(5)
    assert tree.root.value == 5
    assert tree.root.left is None
    assert tree.root.right is None

    tree.add(3)
    assert tree.root.left.value == 3
    assert tree.root.right is None

    tree.add(7)
    assert tree.root.right.value == 7

def test_remove():
    tree = BinaryTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        tree.add(value)

    tree.remove(3)
    assert 3 not in tree
    assert list(tree) == [2, 4, 5, 6, 7, 8]

    tree.remove(5)
    assert 5 not in tree
    assert list(tree) == [2, 4, 6, 7, 8]

def test_get_min_max():
    tree = BinaryTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        tree.add(value)

    assert tree.getMin() == 2
    assert tree.getMax() == 8

def test_contains():
    tree = BinaryTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        tree.add(value)

    assert 3 in tree
    assert 5 in tree
    assert 9 not in tree

def test_closest():
    tree = BinaryTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        tree.add(value)

    assert tree.closest(5) == 5
    assert tree.closest(9) == 8
    assert tree.closest(1) == 2
    assert tree.closest(7.1) == 7
    assert tree.closest(4.5) == 5

def test_call_addToSubTree():
    parent = BinaryNode(1)
    with pytest.raises(TypeError) as typeerror:
        node = BinaryNode.addToSubTree(parent, 2)

def test_call_removeFromParent():
    parent = BinaryNode(1)
    with pytest.raises(TypeError) as typeerror:
        node = BinaryNode.removeFromParent(parent, 2)

def test_call_init():
    with pytest.raises(TypeError) as typeerror:
        tree = BinaryTree.__init__()

def test_getMin_message():
    tree = BinaryTree()

    with pytest.raises(Exception) as exception:
        tree.getMin()
    assert str(exception.value) == "Binary Tree is empty"    

def test_getMax_message():
    tree = BinaryTree()
    
    with pytest.raises(Exception) as exception:
        tree.getMax()
    assert str(exception.value) == "Binary Tree is empty"
