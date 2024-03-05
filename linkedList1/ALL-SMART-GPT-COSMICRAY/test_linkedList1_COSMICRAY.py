import pytest
from linkedList1 import SinglyLinkedList, SinglyLinkedNode, DoublyLinkedList, DoublyLinkedNode

def test_singly_linked_list_getitem_negative_index():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(10)
    singly_linked_list.append(20)
    singly_linked_list.append(30)

    # Ensure that accessing an element at index -1 raises an IndexError
    with pytest.raises(IndexError):
        value = singly_linked_list[-1]

    with pytest.raises(IndexError):
        singly_linked_list.__setitem__(-1,1)

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

def test_doubly_linked_list_insert1():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.insert(6,3)
    assert dll.head.next.next.data == 3
