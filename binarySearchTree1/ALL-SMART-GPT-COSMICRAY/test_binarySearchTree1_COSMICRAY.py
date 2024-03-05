import pytest
from binarySearchTree1 import BinaryNode, BinaryTree

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

def test_contains():
    tree = BinaryTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        tree.add(value)

    assert 3 in tree
    assert 5 in tree
    assert 9 not in tree

def test_remove():
    # Create a binary tree
    tree = BinaryTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        tree.add(value)

    # Test removal of existing and non-existing values
    tree.remove(3)
    assert list(tree) == [2, 4, 5, 6, 7, 8]

    tree.remove(5)
    assert list(tree) == [2, 4, 6, 7, 8]

    tree.remove(4)
    assert list(tree) == [2, 6, 7, 8]

    tree.remove(9)  # Removing non-existing value
    assert list(tree) == [2, 6, 7, 8]

    tree.remove(6)
    assert list(tree) == [2, 7, 8]

    tree.remove(2)
    assert list(tree) == [7, 8]

    tree.remove(7)
    assert list(tree) == [8]

    tree.remove(8)
    assert list(tree) == []

def test_iter():
    # Create a binary tree
    tree = BinaryTree()
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        tree.add(value)

    # Test the iteration
    assert list(iter(tree)) == [2, 3, 4, 5, 6, 7, 8]

    # Remove some values and test again
    tree.remove(3)
    assert list(iter(tree)) == [2, 4, 5, 6, 7, 8]

    tree.remove(5)
    assert list(iter(tree)) == [2, 4, 6, 7, 8]

    tree.remove(8)
    assert list(iter(tree)) == [2, 4, 6, 7]

    # Add more values and test again
    tree.add(1)
    tree.add(9)
    assert list(iter(tree)) == [1, 2, 4, 6, 7, 9]
