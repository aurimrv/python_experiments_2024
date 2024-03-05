import pytest
from queue3 import Node, DoublyLinkedList, Queue

def test_empty_node():
    empty_node = Node(None)

    assert empty_node.value is None
    assert empty_node.next is None
    assert empty_node.prev is None

def test_empty_doubly_linked_list():
    empty_list = DoublyLinkedList()

    removed_head_node = empty_list.removeAtHead()
    removed_tail_node = empty_list.removeAtTail()

    assert removed_head_node is None
    assert removed_tail_node is None
    assert empty_list.getHead() is None
    assert empty_list.getTail() is None
    assert empty_list.getSize() == 0
    assert empty_list.isEmpty() == True

def test_remove_at_tail_single_element():
    single_element_list = DoublyLinkedList()
    single_element_list.addAtTail(1)

    removed_node = single_element_list.removeAtTail()

    assert removed_node.value == 1
    assert single_element_list.getHead() is None
    assert single_element_list.getTail() is None
    assert single_element_list.getSize() == 0
    assert single_element_list.isEmpty() == True

