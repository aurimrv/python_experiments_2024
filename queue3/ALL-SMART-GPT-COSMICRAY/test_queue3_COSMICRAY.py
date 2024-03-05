import pytest
from queue3 import Node, DoublyLinkedList, Queue

def test_remove_at_tail_single_element():
    single_element_list = DoublyLinkedList()
    single_element_list.addAtTail(1)

    removed_node = single_element_list.removeAtTail()

    assert removed_node.value == 1
    assert single_element_list.getHead() is None
    assert single_element_list.getTail() is None
    assert single_element_list.getSize() == 0
    assert single_element_list.isEmpty() == True
