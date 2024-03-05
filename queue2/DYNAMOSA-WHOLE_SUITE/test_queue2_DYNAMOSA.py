#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue2/DYNAMOSA/test_queue2.py.orig
import pytest
import queue2 as module_0

def test_case_0():
    int_0 = 337
    linked_node_0 = module_0.LinkedNode(int_0)
    var_0 = linked_node_0.checkInfinite()
    assert var_0 is False

def test_case_1():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    list_0 = [queue_linked_list_0, queue_linked_list_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 2
    var_0 = linked_list_0.remove(queue_linked_list_0)
    assert var_0 is True
    assert len(linked_list_0) == 1

def test_case_2():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_node_0 = module_0.LinkedNode(linked_list_0)
    assert len(linked_node_0.value) == 0
    var_0 = linked_node_0.checkInfinite()
    assert var_0 is False

def test_case_3():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    with pytest.raises(Exception):
        linked_list_0.pop()

def test_case_4():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.pop()
    assert len(linked_list_0) == 0
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue2.LinkedList'
    assert len(var_1) == 0
    var_2 = linked_list_0.__repr__()
    assert var_2 == 'link:[]'
    bool_0 = True

def test_case_5():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.remove(linked_list_0)
    assert var_0 is False

def test_case_6():
    bool_0 = True
    str_0 = '}z>{XsW2{4"d.Ef^rx'
    none_type_0 = None
    linked_node_0 = module_0.LinkedNode(none_type_0)
    list_0 = [bool_0, str_0]
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    bool_1 = True
    var_0 = linked_list_0.__repr__()
    assert var_0 == 'link:[]'
    tuple_0 = (bool_0, str_0, list_0, bool_1)
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_1 = queue_linked_list_0.__len__()
    assert var_1 == 0

def test_case_7():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.__iter__()
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_1 = linked_list_0.prepend(var_0)
    assert len(linked_list_0) == 1
    linked_list_1 = module_0.LinkedList(*linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 1
    var_2 = linked_list_0.__len__()
    assert var_2 == 1
    var_3 = linked_list_0.prepend(linked_list_1)
    assert len(linked_list_0) == 2

def test_case_8():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__len__()
    assert var_0 == 0
    var_1 = var_0.__repr__()
    assert var_1 == '0'
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_2 = queue_linked_list_0.__len__()
    assert var_2 == 0

def test_case_9():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0]

def test_case_10():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    linked_node_0 = module_0.LinkedNode(queue_linked_list_0, queue_linked_list_0)
    assert len(linked_node_0.value) == 0
    assert len(linked_node_0.next) == 0

def test_case_11():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.__len__()
    assert var_1 == 1
    var_2 = var_0.__repr__()

def test_case_12():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    with pytest.raises(Exception):
        queue_linked_list_0.pop()

def test_case_13():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 2
    linked_node_0 = module_0.LinkedNode(var_0, var_0)
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_2 = linked_list_0.prepend(var_1)
    assert len(linked_list_0) == 1
    var_3 = queue_linked_list_0.__len__()
    assert var_3 == 2
    linked_node_1 = module_0.LinkedNode(linked_list_0, linked_node_0)
    assert len(linked_node_1.value) == 1
    var_4 = linked_node_1.checkInfinite()
    assert var_4 is False
    var_5 = queue_linked_list_0.__iter__()
    var_6 = queue_linked_list_0.pop()
    assert len(queue_linked_list_0) == 1
    assert f'{type(var_6).__module__}.{type(var_6).__qualname__}' == 'queue2.QueueLinkedList'
    assert len(var_6) == 1

def test_case_14():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.isEmpty()
    assert var_1 is False
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_2 = linked_list_0.__repr__()
    assert var_2 == 'link:[]'
    linked_node_0 = module_0.LinkedNode(var_0)
    var_3 = linked_node_0.checkInfinite()
    assert var_3 is False
    var_4 = queue_linked_list_0.__len__()
    assert var_4 == 1
    var_5 = queue_linked_list_0.__len__()
    assert var_5 == 1
    var_6 = queue_linked_list_0.__iter__()
    linked_list_1 = module_0.LinkedList(*var_6)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 1

def test_case_15():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    queue_linked_list_1 = module_0.QueueLinkedList(*queue_linked_list_0)
    assert f'{type(queue_linked_list_1).__module__}.{type(queue_linked_list_1).__qualname__}' == 'queue2.QueueLinkedList'
    assert len(queue_linked_list_1) == 0
    var_0 = queue_linked_list_0.__iter__()
    with pytest.raises(Exception):
        queue_linked_list_0.pop()

def test_case_16():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.__repr__()
    assert var_0 == 'queue:[]'

def test_case_17():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1

def test_case_18():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    list_0 = [queue_linked_list_0, queue_linked_list_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 2
    var_0 = linked_list_0.remove(queue_linked_list_0)
    assert var_0 is True
    assert len(linked_list_0) == 1
    var_1 = queue_linked_list_0.isEmpty()
    assert var_1 is True

def test_case_19():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.isEmpty()
    assert var_1 is False
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_2 = linked_list_0.prepend(var_0)
    assert len(linked_list_0) == 1
    var_3 = queue_linked_list_0.pop()
    assert len(queue_linked_list_0) == 0
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'queue2.QueueLinkedList'
    assert len(var_3) == 0
    var_4 = linked_list_0.__repr__()
    assert var_4 == 'link:[None]'
    linked_node_0 = module_0.LinkedNode(var_0)
    linked_node_1 = module_0.LinkedNode(linked_node_0, var_1)
    assert linked_node_1.next is False
    var_5 = linked_list_0.remove(var_4)
    assert var_5 is False
    var_6 = var_4.__iter__()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0

def test_case_20():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.__iter__()
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_list_1 = module_0.LinkedList(*linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 0
    var_1 = linked_list_0.__len__()
    assert var_1 == 0
    var_2 = linked_list_0.prepend(linked_list_1)
    assert len(linked_list_0) == 1

def test_case_21():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 2
    linked_node_0 = module_0.LinkedNode(var_0, var_0)
    var_2 = queue_linked_list_0.isEmpty()
    assert var_2 is False
    linked_node_1 = module_0.LinkedNode(var_2, linked_node_0)
    assert linked_node_1.value is False
    var_3 = linked_node_1.checkInfinite()
    assert var_3 is False

def test_case_22():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.isEmpty()
    assert var_0 is True
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_1 = linked_list_0.prepend(var_0)
    assert len(linked_list_0) == 1
    var_2 = linked_list_0.__repr__()
    assert var_2 == 'link:[True]'
    linked_node_0 = module_0.LinkedNode(queue_linked_list_0)
    assert len(linked_node_0.value) == 0
    var_3 = queue_linked_list_0.__len__()
    assert var_3 == 0
    linked_node_1 = module_0.LinkedNode(queue_linked_list_0, var_0)
    assert len(linked_node_1.value) == 0
    assert linked_node_1.next is True
    var_4 = linked_list_0.remove(linked_list_0)
    assert var_4 is False

def test_case_23():
    str_0 = 'BStj8I{{'
    list_0 = [str_0, str_0, str_0, str_0]
    float_0 = 1984.509314
    list_1 = [float_0, float_0, float_0]
    linked_list_0 = module_0.LinkedList(*list_1)
    assert len(linked_list_0) == 3
    var_0 = linked_list_0.__repr__()
    assert var_0 == 'link:[1984.509314,1984.509314,1984.509314]'
    var_1 = var_0.__repr__()
    assert var_1 == "'link:[1984.509314,1984.509314,1984.509314]'"

def test_case_24():
    none_type_0 = None
    int_0 = 340
    list_0 = [int_0, int_0, int_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 3
    var_0 = linked_list_0.__len__()
    assert var_0 == 3

def test_case_25():
    bytes_0 = b'\x8b$g\xa6L3Y\x18\xa3N\xf2\xa0\xdd\xb8\xf7\xe9\\4'
    linked_node_0 = module_0.LinkedNode(bytes_0, bytes_0)
    list_0 = [bytes_0, linked_node_0, bytes_0, bytes_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 4
    var_0 = linked_list_0.remove(linked_node_0)
    assert var_0 is True
    assert len(linked_list_0) == 3

def test_case_26():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.isEmpty()
    assert var_0 is True
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_1 = linked_list_0.prepend(var_0)
    assert len(linked_list_0) == 1
    linked_node_0 = module_0.LinkedNode(queue_linked_list_0)
    assert len(linked_node_0.value) == 0
    var_2 = queue_linked_list_0.__len__()
    assert var_2 == 0
    linked_node_1 = module_0.LinkedNode(queue_linked_list_0, var_0)
    assert len(linked_node_1.value) == 0
    assert linked_node_1.next is True
    var_3 = linked_list_0.remove(linked_list_0)
    assert var_3 is False

def test_case_27():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.isEmpty()
    assert var_1 is False
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_2 = linked_list_0.__repr__()
    assert var_2 == 'link:[]'
    linked_node_0 = module_0.LinkedNode(var_0)
    var_3 = linked_node_0.checkInfinite()
    assert var_3 is False
    var_4 = queue_linked_list_0.__len__()
    assert var_4 == 1
    var_5 = queue_linked_list_0.append(var_3)
    assert len(queue_linked_list_0) == 2
    linked_node_1 = module_0.LinkedNode(var_0, var_3)
    var_6 = linked_list_0.remove(var_3)
    assert var_6 is False
    var_7 = queue_linked_list_0.__iter__()
    linked_list_1 = module_0.LinkedList(*var_7)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 2
    var_8 = linked_list_0.__len__()
    assert var_8 == 0
    var_9 = linked_list_0.__len__()
    assert var_9 == 0

def test_case_28():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    linked_node_0 = module_0.LinkedNode(queue_linked_list_0, queue_linked_list_0)
    assert len(linked_node_0.value) == 0
    assert len(linked_node_0.next) == 0
    linked_node_1 = module_0.LinkedNode(queue_linked_list_0, linked_node_0)
    assert len(linked_node_1.value) == 0

def test_case_29():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    linked_node_0 = module_0.LinkedNode(var_0, var_0)
    linked_node_1 = module_0.LinkedNode(queue_linked_list_0, linked_node_0)
    assert len(linked_node_1.value) == 1
    var_1 = linked_node_1.checkInfinite()
    assert var_1 is False
