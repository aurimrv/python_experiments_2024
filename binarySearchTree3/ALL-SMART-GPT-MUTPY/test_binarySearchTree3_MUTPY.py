import pytest
from binarySearchTree3 import NodeDLL, DoubleLinkedList, Queue, Node, Bst

def test_NodeDLL():
    node1 = NodeDLL(1)
    assert repr(node1) == "Value: 1"

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
    assert dll._repr() == [3, 2, 1, 5]
    
    dll = DoubleLinkedList([5, 1, 2, 3])
    dll.shift()
    assert dll._repr() == [3, 2, 1]
    
    dll = DoubleLinkedList([1, 2, 3])
    dll.remove(2)
    assert dll._repr() == [3, 1]

def test_shift():
    # Create a double linked list with some values
    dll = DoubleLinkedList([1, 2, 3, 4])

    # Shift the last element off the tail
    shifted_value = dll.shift()

    # Verify that the shifted value is correct
    assert shifted_value == 1

    # Verify that the tail has been updated correctly
    assert dll.tail.data == 2

def test_remove_tail():
    # Create a double linked list with some values
    dll = DoubleLinkedList([1, 2, 3, 4])

    # Remove the tail element
    dll.remove(1)

    # Verify that the tail has been updated correctly
    assert dll.tail.data == 2

    # Verify the overall content of the list
    assert list(dll._repr()) == [4, 3, 2]

def test_Queue():
    queue = Queue([1, 2, 3])
    assert queue.size() == 3
    assert queue.dequeue() == 3
    assert queue.peek() == 2
    assert queue.size() == 2
    queue.enqueue(4)
    assert queue.size() == 3
    assert queue.dequeue() == 2
    assert queue.dequeue() == 1
    assert queue.dequeue() == 4
    assert queue.size() == 0
    assert queue.peek() is None

def test_Bst():
    bst = Bst([5, 3, 7, 2, 4, 6, 8])

    assert bst.size() == 7
    assert bst.depth() == 3
    assert bst.contains(4) is True
    assert bst.contains(9) is False

    assert bst.balance() == 0

    assert list(bst.in_order()) == [2, 3, 4, 5, 6, 7, 8]
    assert list(bst.pre_order()) == [5, 3, 2, 4, 7, 6, 8]
    assert list(bst.post_order()) == [2, 4, 3, 6, 8, 7, 5]
    assert list(bst.breadth_first()) == [5, 3, 7, 2, 4, 6, 8]

    bst.insert(1)
    bst.insert(9)
    assert list(bst.in_order()) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    bst.delete(5)
    assert list(bst.in_order()) == [1, 2, 3, 4, 6, 7, 8, 9]

def test_call_node_onlychild():
    with pytest.raises(TypeError) as typeerror:
        node = Node._onlychild()

def test_call_bst_findmin():
    node = Node(1)
    with pytest.raises(TypeError) as typeerror:
        bst = Bst._findmin(node)

def test_Node():
    node1 = Node(1)
    assert node1._is_leaf() is True
    assert node1._is_interior() is None
    assert node1._onlychild() is None
    assert node1._side() is None

    node2 = Node(2)
    node1.left = node2
    assert node1._is_leaf() is False
    assert node1._is_interior() is None
    assert node1._onlychild() == 'left'
    assert node2._side() is None

    node3 = Node(3)
    node2.right = node3
    assert node2._onlychild() == 'right'

def test_bst_deletion():
    # Case 1: Deleting a leaf node
    bst_case1 = Bst([5, 3, 7, 2, 4, 6, 8])
    bst_case1.delete(4)
    assert list(bst_case1.in_order()) == [2, 3, 5, 6, 7, 8]
    assert bst_case1._size == 6

    # Case 2: Deleting a node with one child
    bst_case2 = Bst([5, 3, 7, 2, 4, 6, 8])
    bst_case2.delete(7)
    assert list(bst_case2.in_order()) == [2, 3, 4, 5, 6, 8]
    assert bst_case2._size == 6

    # Case 3: Deleting a node with two children
    bst_case3 = Bst([5, 3, 7, 2, 4, 6, 8])
    bst_case3.delete(5)
    assert list(bst_case3.in_order()) == [2, 3, 4, 6, 7, 8]
    assert bst_case3._size == 6

    # Case 4: Deleting the root node with one child
    bst_case4 = Bst([5, 3, 7])
    bst_case4.delete(5)
    assert list(bst_case4.in_order()) == [3, 7]
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

def test_remove_method_mutant():
    dll = DoubleLinkedList()

    with pytest.raises(Exception) as exception:
        dll.remove(1)
    assert str(exception.value) == "1 is not in the list"

def test_findmin_small_tree():
    # Create a small binary search tree
    bst = Bst([8, 3, 10, 1, 6, 9, 12, 2, 5, 7])

    # Call the _findmin method
    min_node = bst._findmin(bst.root)

    # Verify that the minimum node is found correctly
    assert min_node.val == 1

def test_pop_with_new_head_prev():
    # Create a double linked list with some elements
    dll = DoubleLinkedList([1, 2, 3])

    # Call the pop method
    popped_value = dll.pop()

    # Verify that the popped value is correct
    assert popped_value == 3

    # Verify that new_head.prev is set to None
    assert dll.head.prev is None

def test_remove_head():
    # Create a double linked list with some elements
    dll = DoubleLinkedList([1, 2, 3, 4])

    # Call the remove method to remove the head (1)
    dll.remove(4)

    # Verify that the head is updated correctly
    assert dll.head.data == 3
    assert dll.head.prev is None

    # Verify that the length is updated correctly
    assert dll._length == 3

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

def test_find():
    bst = Bst([11, 7, 5, 6, 2, 13])

    no = bst.search(6)
    no = bst._find_replacement(no)

    assert no.val == 7
    assert list(bst.in_order()) == [2, 5, 6, 7, 11, 13]
