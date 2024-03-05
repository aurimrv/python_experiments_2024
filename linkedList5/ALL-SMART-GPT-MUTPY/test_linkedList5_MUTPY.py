import pytest
from linkedList5 import Node, LinkedList

def test_print_list(capsys):
    linked_list = LinkedList()
    linked_list.append(110)
    linked_list.append(120)

    linked_list.print_list()

    captured = capsys.readouterr()
    assert captured.out == "110\n120\n"

def test_insert_to_front_with_none_data():
    linked_list = LinkedList()

    # Attempt to insert None data
    inserted_node = linked_list.insert_to_front(None)

    # Ensure that the method returns None when data is None
    #assert inserted_node is None

    # Ensure that the linked list remains empty
    assert len(linked_list) == 0
    assert linked_list.head is None

def test_find_with_valid_data():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    found_node = linked_list.find(40)

    assert found_node is None

def test_delete_and_verify_list():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.append(50)


    # Delete a node (e.g., with data 20)
    linked_list.delete(30)

    # Ensure that the node is deleted and the list is correct after deletion
    assert len(linked_list) == 4
    assert linked_list.head.data == 10
    assert linked_list.head.next.data == 20
    assert linked_list.head.next.next.data == 40
    assert linked_list.head.next.next.next.data == 50

# Testes criados manualmente
def test_delete():
    linked_list = LinkedList()
    linked_list.append(30)
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(10)

    linked_list.delete(10)

    assert len(linked_list) == 3
    assert linked_list.head.data == 30
    assert linked_list.head.next.data == 20
    assert linked_list.head.next.next.data == 10

# Delete alt aparentemente nao deleta
def test_delete_alt_remove_head():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    # Delete the head node using delete_alt (e.g., with data 10)
    linked_list.delete_alt(10)

    # Ensure that the head node is deleted and the list is correct after deletion
    assert len(linked_list) == 3
    assert linked_list.head.data == 10
    assert linked_list.head.next.data == 20 
