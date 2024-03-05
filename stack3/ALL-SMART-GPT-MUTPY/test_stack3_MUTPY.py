import pytest
from stack3 import Stack, SinglyLinkedList
  
def test_call_init():
    with pytest.raises(TypeError) as typeerror:
        stack = SinglyLinkedList.__init__()

def test_singly_linked_list_add():
    linked_list = SinglyLinkedList()
    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    assert linked_list.toArray() == [3, 2, 1]

    str_representation = str(linked_list)

    assert str_representation == '[3, 2, 1]'

def test_stack_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.__str__() == "[1, 2, 3]"

def test_remove_single_element():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.add(1)

    removed_node = singly_linked_list.remove()

    assert removed_node.value == 1
    assert singly_linked_list.getSize() == 0
    assert singly_linked_list.isEmpty() == True
    assert singly_linked_list.getHead() is None

def test_singly_linked_list_next_values():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.add(1)

    head_node = singly_linked_list.getHeadNode()

    assert head_node.value == 1
    assert head_node.next is None

    singly_linked_list.add(2)
    singly_linked_list.add(3)

    head_node = singly_linked_list.getHeadNode()

    assert head_node.value == 3
    assert head_node.next.value == 2
    assert head_node.next.next.value == 1
    assert head_node.next.next.next is None

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

# Teste criado manualmente
def test_sentinel():
    sll = SinglyLinkedList()
    antes = sll.getHeadNode()

    sll.add(1)

    assert antes.next != None

    sll.add(2)

    assert antes.next == sll.getHeadNode()
    
