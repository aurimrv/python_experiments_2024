import pytest
from linkedList1 import SinglyLinkedList, SinglyLinkedNode, DoublyLinkedList, DoublyLinkedNode

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
