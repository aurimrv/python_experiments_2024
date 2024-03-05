import pytest
from binarySearchTree1 import BinaryTree

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
