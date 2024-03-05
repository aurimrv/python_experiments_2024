import pytest
from linkedList5 import Node, LinkedList

def test_insert_to_front_with_none_data():
    linked_list = LinkedList()

    # Attempt to insert None data
    inserted_node = linked_list.insert_to_front(None)

    # Ensure that the method returns None when data is None
    assert inserted_node is None

    # Ensure that the linked list remains empty
    assert len(linked_list) == 0
    assert linked_list.head is None

def test_append_with_none_data():
    linked_list = LinkedList()

    # Attempt to append None data
    appended_node = linked_list.append(None)

    # Ensure that the method returns None when data is None
    assert appended_node is None

    # Ensure that the linked list remains empty
    assert len(linked_list) == 0
    assert linked_list.head is None

def test_find_with_none_data():
    linked_list = LinkedList()

    # Attempt to find None data
    found_node = linked_list.find(None)

    # Ensure that the method returns None when data is None
    assert found_node is None

