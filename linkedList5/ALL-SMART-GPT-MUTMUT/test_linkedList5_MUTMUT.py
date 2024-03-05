import pytest
import io
import sys
from linkedList5 import Node, LinkedList

def test_delete_with_multiple_elements():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    # Delete a node (e.g., with data 20)
    linked_list.delete(20)

    # Ensure that the node is deleted and the list is correct after deletion
    assert len(linked_list) == 2
    assert linked_list.head.data == 10
    assert linked_list.head.next.data == 30

def test_delete_alt_with_multiple_elements():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    # Delete a node (e.g., with data 20) using delete_alt
    linked_list.delete_alt(20)

    # Ensure that the node is deleted and the list is correct after deletion
    assert len(linked_list) == 2
    assert linked_list.head.data == 10
    assert linked_list.head.next.data == 30

def test_print_list_with_multiple_elements(capsys):
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    # Capture the printed output of print_list
    linked_list.print_list()

    captured = capsys.readouterr()

    # Ensure that the printed output matches the expected result
    assert captured.out == "10\n20\n30\n"

##VERIFICAR O USO DE IO E SYS ACIMA E AS INCONSISTENCIAS DO RELATORIO
