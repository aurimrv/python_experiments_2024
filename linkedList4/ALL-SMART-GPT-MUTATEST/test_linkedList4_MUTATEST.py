import pytest
from linkedList4 import LinkedList, Node

def test_empty_node_creation():
    empty_node = Node(None)

    # Ensure that the data and next values of the empty node are None
    assert empty_node.data is None
    assert empty_node.next is None

def test_remove():
    linked_list = LinkedList([10, 20, 30])
    linked_list.remove(10)

    assert linked_list.size() == 2
    assert linked_list.search(10) is None

def test_remove_head():
    linked_list = LinkedList([10, 20, 30])
    linked_list.remove(30)

    # Ensure that the head is removed, and the list is correct after removal
    assert linked_list.size() == 2
    assert linked_list.search(30) is None
    assert linked_list.head.data == 20
    assert linked_list.head.next.data == 10

