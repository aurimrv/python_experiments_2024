import pytest
from linkedList4 import LinkedList, Node

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

# The below tests were created manually to kill specific mutants
def test_remove_head_is():
    lista = LinkedList()
    lista.push('Lucca')
    lista.push('Auri')
    lista.push('Joao')

    string1 = "Joao"
    help_list = list(string1)
    string2 = ''.join(help_list)

    lista.remove(string2)
    
    assert lista.size() == 2

def test_remove_middle_is():
    lista = LinkedList()
    lista.push('Lucca')
    lista.push('Auri')
    lista.push('Joao')

    string1 = "Lucca"
    help_list = list(string1)
    string2 = ''.join(help_list)

    lista.remove(string2)
    
    assert lista.size() == 2

def test_remove_search_is():
    lista = LinkedList()
    lista.push('Lucca')
    lista.push('Auri')
    lista.push('Joao')

    string1 = "Lucca"
    help_list = list(string1)
    string2 = ''.join(help_list)

    assert lista.search(string2) is not None


