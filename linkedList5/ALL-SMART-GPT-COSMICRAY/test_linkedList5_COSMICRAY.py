import pytest
from linkedList5 import Node, LinkedList

# The below tests were created manually to kill specific mutants
def test_remove_head_is():
    lista = LinkedList()
    lista.append('Lucca')
    lista.append('Auri')
    lista.append('Joao')

    string1 = "Joao"
    help_list = list(string1)
    string2 = ''.join(help_list)

    lista.delete(string2)
    
    assert lista.get_all_data() == ['Lucca', 'Auri']

def test_remove_middle_is():
    lista = LinkedList()
    lista.append('Lucca')
    lista.append('Auri')
    lista.append('Joao')

    string1 = "Lucca"
    help_list = list(string1)
    string2 = ''.join(help_list)

    lista.delete(string2)
    
    assert lista.get_all_data() == ['Auri', 'Joao']

def test_remove_search_is():
    lista = LinkedList()
    lista.append('Lucca')
    lista.append('Auri')
    lista.append('Joao')

    string1 = "Lucca"
    help_list = list(string1)
    string2 = ''.join(help_list)

    assert lista.find(string2) is not None
