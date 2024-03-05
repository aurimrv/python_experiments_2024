import pytest
from binarySearchTree1 import BinaryNode, BinaryTree
def test_empty_tree():
    tree = BinaryTree()
    assert list(tree) == []

def test_sample_tree():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)

    assert list(tree) == [2, 3, 4, 5, 6, 7, 8]

    tree.remove(5)
    assert list(tree) == [2, 3, 4, 6, 7, 8]

    tree.remove(4)
    assert list(tree) == [2, 3, 6, 7, 8]

    tree.remove(6)
    assert list(tree) == [2, 3, 7, 8]

    assert tree.getMin() == 2
    assert tree.getMax() == 8

    assert 3 in tree
    assert 9 not in tree

    assert tree.closest(5) == 3
    assert tree.closest(2) == 2
    assert tree.closest(8) == 8
    assert tree.closest(1) == 2
    assert tree.closest(9) == 8
    assert tree.closest(4.5) == 3
    assert tree.closest(6.5) == 7

def test_empty_tree_closest():
    tree = BinaryTree()
    assert tree.closest(5) is None

def test_closest_single_node_tree():
    tree = BinaryTree()
    tree.add(5)
    assert tree.closest(5) == 5
    assert tree.closest(3) == 5
    assert tree.closest(8) == 5

def test_closest_multiple_nodes_tree():
    tree = BinaryTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)

    assert tree.closest(1) == 2
    assert tree.closest(9) == 8
    assert tree.closest(4.5) == 5
    assert tree.closest(6.5) == 7
