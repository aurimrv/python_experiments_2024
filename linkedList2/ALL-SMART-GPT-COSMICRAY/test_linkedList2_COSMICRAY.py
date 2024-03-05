import pytest
from linkedList2 import LinkedNode, LinkedList

def test_check_infinite_with_loop():
    # Create a linked list with an infinite loop
    node1 = LinkedNode(1)
    node2 = LinkedNode(2)
    node1.next = node2
    node2.next = node1

    assert node1.checkInfinite()

def test_check_infinite_with_loop1():
    # Create a linked list with an infinite loop
    node1 = LinkedNode(1)
    node2 = LinkedNode(2)
    node1.next = node2
    node2.next = node2

    assert node1.checkInfinite()


