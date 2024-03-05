#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/queue2/MIO/test_queue2.py.orig
import pytest
import queue2 as module_0
import builtins as module_1

def test_case_0():
    int_0 = -1081
    linked_node_0 = module_0.LinkedNode(int_0)
    var_0 = linked_node_0.checkInfinite()
    assert var_0 is False

def test_case_1():
    bool_0 = True
    linked_node_0 = module_0.LinkedNode(bool_0, bool_0)

def test_case_2():
    bool_0 = True
    linked_node_0 = module_0.LinkedNode(bool_0)
    linked_node_1 = module_0.LinkedNode(bool_0, linked_node_0)
    var_0 = linked_node_1.checkInfinite()
    assert var_0 is False

def test_case_3():
    bool_0 = True
    linked_node_0 = module_0.LinkedNode(bool_0, bool_0)
    linked_node_1 = module_0.LinkedNode(bool_0, linked_node_0)

def test_case_4():
    bytes_0 = b'\x87V\xbbe\nR'
    linked_list_0 = module_0.LinkedList(*bytes_0)
    assert len(linked_list_0) == 6

def test_case_5():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0

def test_case_6():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    with pytest.raises(Exception):
        linked_list_0.pop()

def test_case_7():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.pop()
    assert len(linked_list_0) == 0
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue2.LinkedList'
    assert len(var_1) == 0

def test_case_8():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.remove(linked_list_0)
    assert var_1 is True
    assert len(linked_list_0) == 0

def test_case_9():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.remove(var_0)
    assert var_1 is False

def test_case_10():
    str_0 = 'aURNHB^'
    linked_list_0 = module_0.LinkedList(*str_0)
    assert len(linked_list_0) == 7
    var_0 = linked_list_0.remove(str_0)
    assert var_0 is False

def test_case_11():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.remove(linked_list_0)
    assert var_0 is False

def test_case_12():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 2
    var_0 = linked_list_0.__repr__()
    assert var_0 == 'link:[False,False]'

def test_case_13():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_list_1 = module_0.LinkedList(*linked_list_0)
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'queue2.LinkedList'
    assert len(linked_list_1) == 0

def test_case_14():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__repr__()
    assert var_0 == 'link:[]'

def test_case_15():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    linked_list_0 = module_0.LinkedList(*list_0)
    assert len(linked_list_0) == 2
    var_0 = linked_list_0.__len__()
    assert var_0 == 2

def test_case_16():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1
    var_1 = linked_list_0.__len__()
    assert var_1 == 1

def test_case_17():
    bytes_0 = b'D\xa2\xd8\xa8n\xf3\x06\xf2\xa8\x91\xe4i\x00\xdd\xcd'

def test_case_18():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0

def test_case_19():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1

def test_case_20():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.append(var_0)
    assert len(queue_linked_list_0) == 2

def test_case_21():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.pop()
    assert len(queue_linked_list_0) == 0
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'queue2.QueueLinkedList'
    assert len(var_1) == 0

def test_case_22():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 2
    var_2 = queue_linked_list_0.pop()
    assert len(queue_linked_list_0) == 1
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'queue2.QueueLinkedList'
    assert len(var_2) == 1

def test_case_23():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    with pytest.raises(Exception):
        queue_linked_list_0.pop()

def test_case_24():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 2

def test_case_25():
    bool_0 = True
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(bool_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.__repr__()
    assert var_1 == 'queue:[True]'
    var_2 = var_1.__repr__()
    assert var_2 == "'queue:[True]'"

def test_case_26():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1

def test_case_27():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    object_0 = module_1.object(*queue_linked_list_0)

def test_case_28():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.__repr__()
    assert var_0 == 'queue:[]'

def test_case_29():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.append(queue_linked_list_0)
    assert len(queue_linked_list_0) == 1
    var_1 = queue_linked_list_0.__len__()
    assert var_1 == 1

def test_case_30():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.__len__()
    assert var_0 == 0

def test_case_31():
    int_0 = -1124
    linked_node_0 = module_0.LinkedNode(int_0)

def test_case_32():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.prepend(linked_list_0)
    assert len(linked_list_0) == 1

def test_case_33():
    queue_linked_list_0 = module_0.QueueLinkedList()
    assert len(queue_linked_list_0) == 0
    var_0 = queue_linked_list_0.isEmpty()
    assert var_0 is True
