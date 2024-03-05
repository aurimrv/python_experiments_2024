import pytest
from queue3 import Node, DoublyLinkedList, Queue

def test_doubly_linked_list_str():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.addAtTail(1)
    doubly_linked_list.addAtTail(2)
    doubly_linked_list.addAtTail(3)

    str_representation = str(doubly_linked_list)

    assert str_representation == '[1, 2, 3]'

def test_empty_node():
    empty_node = Node(None)

    assert empty_node.value is None
    assert empty_node.next is None
    assert empty_node.prev is None

def test_remove_at_head():
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.addAtTail(1)
    doubly_linked_list.addAtTail(2)
    doubly_linked_list.addAtTail(3)

    removed_node = doubly_linked_list.removeAtHead()

    assert removed_node.value == 1
    assert doubly_linked_list.getHead() == 2
    assert doubly_linked_list.getTail() == 3
    assert doubly_linked_list.getSize() == 2
    assert str(doubly_linked_list) == '[2, 3]'

def test_remove_at_tail_single_element():
    single_element_list = DoublyLinkedList()
    single_element_list.addAtTail(1)

    removed_node = single_element_list.removeAtTail()

    assert removed_node.value == 1
    assert single_element_list.getHead() is None
    assert single_element_list.getTail() is None
    assert single_element_list.getSize() == 0
    assert single_element_list.isEmpty() == True

