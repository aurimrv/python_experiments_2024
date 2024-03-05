#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue3/MIO/test_queue3.py.orig
import pytest
import queue3 as module_0

def test_case_0():
    queue_0 = module_0.Queue()

def test_case_1():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtHead(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1

def test_case_2():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    none_type_1 = doubly_linked_list_0.addAtHead(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 2

def test_case_3():
    queue_0 = module_0.Queue()
    none_type_0 = queue_0.enqueue(queue_0)

def test_case_4():
    queue_0 = module_0.Queue()
    none_type_0 = queue_0.enqueue(queue_0)
    none_type_1 = queue_0.enqueue(queue_0)

def test_case_5():
    queue_0 = module_0.Queue()
    none_type_0 = queue_0.enqueue(queue_0)
    var_0 = queue_0.dequeue()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'queue3.Queue'
    assert var_0.next is None
    assert var_0.prev is None

def test_case_6():
    queue_0 = module_0.Queue()
    none_type_0 = queue_0.enqueue(queue_0)
    none_type_1 = queue_0.enqueue(none_type_0)
    var_0 = queue_0.dequeue()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'queue3.Queue'
    assert var_0.next is None
    assert var_0.prev is None

def test_case_7():
    queue_0 = module_0.Queue()
    var_0 = queue_0.dequeue()

def test_case_8():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtHead(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    var_0 = doubly_linked_list_0.removeAtTail()
    assert len(doubly_linked_list_0) == 0
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_0.value) == 0
    assert var_0.next is None
    assert var_0.prev is None

def test_case_9():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    none_type_1 = doubly_linked_list_0.addAtHead(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 2
    var_0 = doubly_linked_list_0.removeAtTail()
    assert len(doubly_linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.Node'
    assert f'{type(var_0.value).__module__}.{type(var_0.value).__qualname__}' == 'queue3.DoublyLinkedList'
    assert len(var_0.value) == 1
    assert var_0.next is None
    assert var_0.prev is None

def test_case_10():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    var_0 = doubly_linked_list_0.removeAtTail()

def test_case_11():
    queue_0 = module_0.Queue()
    bool_0 = queue_0.isEmpty()
    assert bool_0 is True

def test_case_12():
    queue_0 = module_0.Queue()
    none_type_0 = queue_0.enqueue(queue_0)
    bool_0 = queue_0.isEmpty()
    assert bool_0 is False

def test_case_13():
    queue_0 = module_0.Queue()
    var_0 = queue_0.getHead()

def test_case_14():
    queue_0 = module_0.Queue()
    none_type_0 = queue_0.enqueue(queue_0)
    var_0 = queue_0.getHead()
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'queue3.Queue'

def test_case_15():
    queue_0 = module_0.Queue()
    none_type_0 = queue_0.enqueue(queue_0)
    none_type_1 = queue_0.enqueue(queue_0)
    str_0 = queue_0.__str__()

def test_case_16():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    none_type_0 = doubly_linked_list_0.addAtTail(doubly_linked_list_0)
    assert len(doubly_linked_list_0) == 1
    str_0 = doubly_linked_list_0.__str__()

def test_case_17():
    queue_0 = module_0.Queue()
    str_0 = queue_0.__str__()
    assert str_0 == '[]'

def test_case_18():
    queue_0 = module_0.Queue()
    var_0 = queue_0.getTail()

def test_case_19():
    queue_0 = module_0.Queue()
    int_0 = queue_0.getSize()
    assert int_0 == 0

def test_case_20():
    doubly_linked_list_0 = module_0.DoublyLinkedList()
    assert len(doubly_linked_list_0) == 0
    int_0 = doubly_linked_list_0.__len__()
    assert int_0 == 0
