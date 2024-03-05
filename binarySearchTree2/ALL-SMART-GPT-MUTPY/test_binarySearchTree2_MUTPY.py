import pytest
from binarySearchTree2 import Node, BST

def test_call_bst_init():
    with pytest.raises(TypeError) as typeerror:
        bst = BST.__init__()

def test_call_bst_min():
    node = Node(1)
    with pytest.raises(TypeError) as typeerror:
        bst = BST.minValueNode(node)

def test_call_bst_valid():
    with pytest.raises(TypeError) as typeerror:
        bst = BST.isValid()

def test_add_multiple_elements():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    assert bst.getOrder() == [3, 5, 7]
    assert len(bst) == 3

def test_remove_leaf_node():
    bst = BST()
    bst.add(5)
    bst.remove(5)
    assert bst.getOrder() == []
    assert len(bst) == 0

def test_remove_node_with_two_children():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.remove(5)
    assert bst.getOrder() == [3, 7]
    assert len(bst) == 2

def test_str_representation(capsys):
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    print(bst)
    captured = capsys.readouterr()
    assert captured.out.strip() == "[3, 5, 7]"

def test_getOrder_postOrder():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    assert bst.getOrder(order="postOrder") == [3, 7, 5]

def test_getOrder_preOrder():
    bst = BST()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    assert bst.getOrder(order="preOrder") == [5, 3, 7]

def test_minValueNode_large_tree():
    bst = BST()
    values = [10, 5, 15, 3, 7, 12, 20, 2, 8, 11, 18, 25]
    for value in values:
        bst.add(value)

    min_node = bst.minValueNode(bst.root)
    assert min_node.value == 2

def test_remove_root_large_tree():
    bst = BST()
    values = [10, 5, 15, 3, 7, 12, 20, 2, 8, 11, 18, 25]
    for value in values:
        bst.add(value)

    bst.remove(10)  # Removing the root

    assert bst.getOrder() == [2, 3, 5, 7, 8, 11, 12, 15, 18, 20, 25]
    assert len(bst) == 11

def test_remove_node_to_right_large_tree():
    bst = BST()
    values = [10, 5, 15, 3, 7, 12, 20, 2, 8, 11, 18, 25]
    for value in values:
        bst.add(value)

    bst.remove(15)  # Removing a node to the right of the root

    assert bst.getOrder() == [2, 3, 5, 7, 8, 10, 11, 12, 18, 20, 25]
    assert len(bst) == 11  # Updated length after removal



