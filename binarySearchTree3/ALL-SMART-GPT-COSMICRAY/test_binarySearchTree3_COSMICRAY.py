import pytest
from binarySearchTree3 import NodeDLL, DoubleLinkedList, Queue, Node, Bst

def test_find():
    bst = Bst([11, 7, 5, 6, 2, 13])

    no = bst.search(6)
    no = bst._find_replacement(no)

    assert no.val == 7
    assert list(bst.in_order()) == [2, 5, 6, 7, 11, 13]

def test_find_replacement_left_side():
    # Create a BST with some nodes
    bst = Bst([5, 3, 7, 2, 4, 6, 8, 1, 9])

    # Get a reference to a node with only a left child
    node_with_left_child = bst.search(2)

    # Original code should correctly find the replacement when node.parent is true and node.side is left
    result = bst._find_replacement(node_with_left_child)

    # Verify that the result is as expected (leftmost node of the right subtree)
    assert result.val == 3
    assert result.right.val == 4

def test_bst_find_replacement():
    # Case 1: Node with two children
    bst_case1 = Bst([5, 3, 7, 2, 4, 6, 8])
    node_to_delete_case1 = bst_case1.search(5)
    replacement_case1 = bst_case1._find_replacement(node_to_delete_case1)
    assert replacement_case1 is not None
    assert replacement_case1.val == 6

    # Case 2: Node with left subtree
    bst_case2 = Bst([8, 3, 10, 2, 6, 9, 11, 1, 5, 7])
    node_to_delete_case2 = bst_case2.search(8)
    replacement_case2 = bst_case2._find_replacement(node_to_delete_case2)
    assert replacement_case2 is not None
    assert replacement_case2.val == 9

    # Case 3: Node with right subtree
    bst_case3 = Bst([8, 3, 10, 2, 6, 9, 11, 1, 5, 7])
    node_to_delete_case3 = bst_case3.search(10)
    replacement_case3 = bst_case3._find_replacement(node_to_delete_case3)
    assert replacement_case3 is not None
    assert replacement_case3.val == 11

def test_shift_two_element_list():
    # Create a DLL with two elements
    dll = DoubleLinkedList([1, 2])

    # Test shift method for a two-element list
    shifted_value = dll.shift()

    # Verify the shifted value
    assert shifted_value == 1

    # Verify the head and tail values after shifting
    assert dll.head.data == 2
    assert dll.tail.data == 2

def test_DoubleLinkedList():
    dll = DoubleLinkedList([1, 2, 3])
    assert dll._repr() == [3, 2, 1]
    
    dll = DoubleLinkedList([1, 2, 3])
    dll.push(4)
    assert dll._repr() == [4, 3, 2, 1]

    dll = DoubleLinkedList([1, 2, 3, 4])
    dll.append(5)
    assert dll._repr() == [4, 3, 2, 1, 5]

    dll = DoubleLinkedList([5, 1, 2, 3, 4])
    dll.pop()
    assert dll.head.prev is None
    assert dll._repr() == [3, 2, 1, 5]

    dll = DoubleLinkedList([5, 1, 2, 3])
    dll.shift()
    assert dll.tail is not None
    assert dll.tail.next is None
    assert dll._length == 3
    assert dll._repr() == [3, 2, 1]
    
    dll = DoubleLinkedList([1, 2, 3])
    dll.remove(2)
    assert dll._repr() == [3, 1]

    dll = DoubleLinkedList([1, 2, 3, 4])
    dll.remove(1)
    assert dll._repr() == [4, 3, 2]

def test_remove_tail():
    # Create a double linked list with some values
    dll = DoubleLinkedList([1, 2, 3, 4])

    # Remove the tail element
    dll.remove(1)

    # Verify that the tail has been updated correctly
    assert dll.tail.data == 2
    assert dll.tail.next is None

    # Verify the overall content of the list
    assert list(dll._repr()) == [4, 3, 2]

def test_remove_head():
    # Create a double linked list with some values
    dll = DoubleLinkedList([1, 2, 3, 4])

    # Remove the tail element
    dll.remove(4)

    # Verify that the tail has been updated correctly
    assert dll.head.data == 3
    assert dll.head.prev is None

    # Verify the overall content of the list
    assert list(dll._repr()) == [3, 2, 1]

def test_pre_order_non_empty_tree():
    # Create a non-empty BST
    bst = Bst([5, 3, 7, 2, 4, 6, 8])

    # Test pre_order method for a non-empty tree
    result = list(bst.pre_order())
    assert result == [5, 3, 2, 4, 7, 6, 8] 

def test_bst_onlychild():
    # Create a sample BST
    bst = Bst([5, 3, 7, 2, 8])
    root = bst.root

    # Test _onlychild method
    assert root.left._onlychild() == 'left'
    assert root.right._onlychild() == 'right'
    assert root._onlychild() is None
    assert root.right.right._onlychild() is None

def test_breadth_first_non_empty_tree():
    # Create a non-empty BST
    bst = Bst([5, 3, 7, 2, 4, 6, 8])

    # Test breadth_first method for a non-empty tree
    result = list(bst.breadth_first())
    assert result == [5, 3, 7, 2, 4, 6, 8]

def test_breadth_first_only_right_nodes():
    # Create a BST with only right nodes
    bst = Bst([1, 2, 3, 4, 5])

    # Test breadth_first method for a tree with only right nodes
    result = list(bst.breadth_first())
    assert result == [1, 2, 3, 4, 5]

def test_delete_root_with_one_child():
    # Create a binary search tree with a one-sided structure
    bst = Bst([5, 3, 2, 1])

    # Remove the root node (5) with one child
    bst.delete(5)

    # Verify that the root is updated correctly
    assert bst.root.val == 3
    assert bst.root.left.val == 2
    assert bst.root.left.parent == bst.root
    assert bst.root.left.left.val == 1
    assert bst.root.left.left.parent == bst.root.left

    # Verify the size is updated correctly
    assert bst.size() == 3

def test_delete_single_child():
    # Create a BST with some nodes
    bst = Bst([5, 3, 7, 2, 4, 6, 8, 1, 9])

    # Delete a node with only one child (node with value 2)
    bst.delete(2)

    # Verify that the deleted node's parent now points to the single child (1)
    assert bst.search(1).left is None
    assert bst.search(1).parent.val == 3  

    # Verify that the root is updated correctly
    assert bst.root.val == 5

def test_delete_non_root_with_one_child():
    # Create a binary search tree with some elements
    bst = Bst([5, 3, 8, 2, 7, 9])

    # Remove a non-root node (3) with one child
    bst.delete(3)

    # Verify that the tree structure is updated correctly
    assert bst.root.val == 5
    assert bst.root.left.val == 2
    assert bst.root.left.parent == bst.root
    assert bst.root.left.left is None

    # Verify the size is updated correctly
    assert bst.size() == 5

def test_bst_deletion():
    # Case 3: Deleting a node with two children
    bst_case3 = Bst([5, 3, 7, 2, 4, 6, 8])
    bst_case3.delete(5)
    assert list(bst_case3.in_order()) == [2, 3, 4, 6, 7, 8]
    assert bst_case3._size == 6

def test_Bst_post_order():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])

    assert list(bst.post_order()) == [2, 4, 3, 6, 8, 7, 5]
