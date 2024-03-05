import pytest
from queue3 import Node, DoublyLinkedList, Queue

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
