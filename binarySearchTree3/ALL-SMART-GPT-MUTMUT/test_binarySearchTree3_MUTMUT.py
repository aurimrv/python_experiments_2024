import pytest
from binarySearchTree3 import NodeDLL, DoubleLinkedList, Queue, Node, Bst

def test_pop_method_mutant():
    dll = DoubleLinkedList()

    with pytest.raises(Exception) as exception:
        dll.pop()
    assert str(exception.value) == "Cannot pop from an empty list."

def test_shift_method_mutant():
    dll = DoubleLinkedList()

    with pytest.raises(Exception) as exception:
        dll.shift()
    assert str(exception.value) == "Cannot shift from an empty list."

def test_remove_method_mutant():
    dll = DoubleLinkedList()

    with pytest.raises(Exception) as exception:
        dll.remove(1)
    assert str(exception.value) == "1 is not in the list"

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

def test_empty_node():
    # Create an empty node
    empty_node = Node()

    # Verify that the node is empty
    assert empty_node.val is None
    assert empty_node.left is None
    assert empty_node.right is None
    assert empty_node.parent is None
    assert empty_node.height == 1

def test_bst_node_properties():
    # Create a sample BST
    bst = Bst([5, 3, 7, 2, 4, 6, 8])
    root = bst.root

    # Test _is_leaf method
    assert root._is_leaf() is False
    assert root.left.left._is_leaf() is True

    # Test _is_interior method
    assert root._is_interior() is not None
    assert root.left.left._is_interior() is None

    # Test _onlychild method
    assert root.left.left._onlychild() is None
    assert root.right._onlychild() is None
    assert root._onlychild() is None

    # Test _side method
    assert root.left._side() == 'left'
    assert root.right.right._side() == 'right'
    assert root._side() is None

def test_bst_deletion():
    # Case 1: Deleting a leaf node
    bst_case1 = Bst([5, 3, 7, 2, 4, 6, 8])
    bst_case1.delete(4)
    assert list(bst_case1.in_order()) == [2, 3, 5, 6, 7, 8]
    assert bst_case1._size == 6

    # Case 2: Deleting a node with one child
    bst_case2 = Bst([5, 3, 7, 2, 4, 8])
    bst_case2.delete(7)
    assert list(bst_case2.in_order()) == [2, 3, 4, 5, 8]
    assert bst_case2._size == 5

    # Case 3: Deleting a node with two children
    bst_case3 = Bst([5, 3, 7, 2, 4, 6, 8])
    bst_case3.delete(5)
    assert list(bst_case3.in_order()) == [2, 3, 4, 6, 7, 8]
    assert bst_case3._size == 6

    # Case 4: Deleting the root node with one child
    bst_case4 = Bst([5, 7, 8])
    bst_case4.delete(5)
    assert list(bst_case4.in_order()) == [7, 8]
    assert bst_case4._size == 2

    # Case 5: Deleting the root node with two children
    bst_case5 = Bst([5, 3, 7, 2, 4, 6, 8])
    bst_case5.delete(5)
    assert list(bst_case5.in_order()) == [2, 3, 4, 6, 7, 8]
    assert bst_case5._size == 6

    # Case 6: Deleting a non-existent node
    bst_case6 = Bst([5, 3, 7, 2, 4, 6, 8])
    bst_case6.delete(9)
    assert list(bst_case6.in_order()) == [2, 3, 4, 5, 6, 7, 8]
    assert bst_case6._size == 7

def test_pre_order_non_empty_tree():
    # Create a non-empty BST
    bst = Bst([5, 3, 7, 2, 4, 6, 8])

    # Test pre_order method for a non-empty tree
    result = list(bst.pre_order())
    assert result == [5, 3, 2, 4, 7, 6, 8] 

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

def test_find_replacement_left_side():
    # Create a BST with some nodes
    bst = Bst([5, 3, 7, 2, 4, 6, 8, 1, 9])

    # Get a reference to a node with only a left child
    node_with_left_child = bst.search(2)

    result = bst._find_replacement(node_with_left_child)

    # Verify that the result is as expected (leftmost node of the right subtree)
    assert result.val == 3
    assert result.right.val == 4

def test_find():
    bst = Bst([11, 7, 5, 6, 2, 13])

    no = bst.search(6)
    no = bst._find_replacement(no)

    assert no.val == 7
    assert list(bst.in_order()) == [2, 5, 6, 7, 11, 13]

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

def test_shift_with_two_elements():
    # Create a double linked list with two elements
    dll = DoubleLinkedList([1, 2])

    # Perform the shift operation
    shifted_value = dll.shift()

    # Verify that the shifted value is correct
    assert shifted_value == 1

    # Verify that the tail is updated correctly
    assert dll.tail.data == 2
    assert dll.tail.next is None
    assert dll._length == 1

def test_remove_tail():
    # Create a double linked list with some values
    dll = DoubleLinkedList([1, 2, 3, 4])

    # Remove the tail element
    dll.remove(1)

    # Verify that the tail has been updated correctly
    assert dll.tail.data == 2

    # Verify the overall content of the list
    assert list(dll._repr()) == [4, 3, 2]

