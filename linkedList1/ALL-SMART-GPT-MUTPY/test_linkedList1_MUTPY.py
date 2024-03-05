import pytest
from linkedList1 import SinglyLinkedList, SinglyLinkedNode, DoublyLinkedList, DoublyLinkedNode

def test_call_init():
    with pytest.raises(TypeError) as typeerror:
        sll = SinglyLinkedList.__init__()

# Manually created tests 
def test_doubly_linked_list_insert():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.insert(4,0)
    assert dll.head.data == 4
    assert dll.head.next.prev.data == 4

    dll.insert(5,3)
    assert dll.head.next.next.next.next.data == 5

    dll.insert(6,2)
    assert dll.head.next.next.data == 6
    assert dll.head.next.next.prev.data == 1
    assert dll.head.next.next.next.prev.data == 6
    assert dll.head.next.next.next.next.next.data == 5

def test_singly_linked_list_insert():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    assert sll.head.next.next.data == 3
    sll.__setitem__(0,4)
    assert sll.head.data == 4

    sll.__setitem__(2,5)
    assert sll.head.next.next.data == 5

def test_singly_linked_list_insert1():
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(4)
    sll.append(5)
    assert sll.head.next.next.next.data == 4

def test_doubly_linked_list_insert2():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.insert(6,3)
    assert dll.head.next.next.data == 3

def test_doubly_linked_list_insert_cursor():
    dll = DoublyLinkedList()

    dll.insert(1,-1)
    
    assert dll.cursor.data == dll.head.data
