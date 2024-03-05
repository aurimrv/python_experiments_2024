import pytest
from linkedList3 import Node, SinglyLinkedList

def test_remove_single_element():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.add(1)

    removed_node = singly_linked_list.remove()

    assert removed_node.value == 1
    assert singly_linked_list.getSize() == 0
    assert singly_linked_list.isEmpty() == True
    assert singly_linked_list.getHead() is None

def test_remove_multiple_elements_small_list():
    singly_linked_list = SinglyLinkedList()

    singly_linked_list.add(1)
    singly_linked_list.add(2)
    singly_linked_list.add(3)
    singly_linked_list.add(4)
    singly_linked_list.add(5)

    assert singly_linked_list.getHead() == 5

    singly_linked_list.remove()
    singly_linked_list.remove()

    assert singly_linked_list.getHead() == 3
    assert singly_linked_list.getSize() == 3

def test_to_array():
    linked_list = SinglyLinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    array_representation = linked_list.toArray()

    assert array_representation == [3, 2, 1]

    str_representation = str(linked_list)

    assert str_representation == '[3, 2, 1]'
