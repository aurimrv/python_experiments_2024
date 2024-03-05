import pytest
from binarySearchTree4 import Bst, Node

@pytest.fixture
def bst_with_root():
    # Create a BST with a root node containing data 5
    return Bst(Node(5))

def test_insert_left(bst_with_root):
    # Insert a new node with data 3
    new_node = bst_with_root.insert(3)

    # Check that the new node is the left child of the root
    assert bst_with_root.root.left == new_node

    # Check that the parent attribute of the new node is set correctly
    assert new_node.parent == bst_with_root.root

def test_insert_right(bst_with_root):
    # Insert a new node with data 8
    new_node = bst_with_root.insert(8)

    # Check that the new node is the right child of the root
    assert bst_with_root.root.right == new_node

    # Check that the parent attribute of the new node is set correctly
    assert new_node.parent == bst_with_root.root

@pytest.fixture
def bst_with_existing_right_child():
    # Create a BST with a root node containing data 5 and a right child containing data 10
    bst = Bst(Node(5))
    bst.root.right = Node(10)
    return bst

def test_insert_right_mutant(bst_with_existing_right_child):
    # Insert a new node with data 10 (same as existing right child)
    mutated_node = bst_with_existing_right_child.insert(10)

    # Check that the mutated node is the left child of the root
    assert bst_with_existing_right_child.root.right.left == mutated_node

    # Check that the parent attribute of the mutated node is set correctly
    assert mutated_node.parent == bst_with_existing_right_child.root.right

@pytest.fixture
def bst_with_existing_left_child():
    # Create a BST with a root node containing data 5 and a left child containing data 3
    bst = Bst(Node(5))
    bst.root.left = Node(3)
    return bst

def test_insert_left_mutant(bst_with_existing_left_child):
    # Insert a new node with data 2 (less than the existing left child)
    mutated_node = bst_with_existing_left_child.insert(2)

    # Check that the mutated node is the left child of the existing left child
    assert bst_with_existing_left_child.root.left.left == mutated_node

    # Check that the parent attribute of the mutated node is set correctly
    assert mutated_node.parent == bst_with_existing_left_child.root.left



