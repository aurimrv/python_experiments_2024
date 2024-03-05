#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList5/WHOLE_SUITE/test_linkedList5.py.orig
import pytest
import linkedList5 as module_0

def test_case_0():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_0 = linked_list_1.get_all_data()
    var_1 = linked_list_0.find(linked_list_0)
    var_2 = linked_list_0.delete(var_0)
    var_3 = var_0.__len__()

def test_case_1():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 2
    assert len(var_0.data) == 2
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1.data) == 2
    var_2 = linked_list_0.print_list()

def test_case_2():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 2
    assert len(var_0.data) == 2
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1.data) == 2
    var_2 = linked_list_0.print_list()
    var_3 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 3
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_0.data) == 3
    assert len(var_1.data) == 3
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert var_3.next is None
    assert f'{type(var_3.data).__module__}.{type(var_3.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_3.data) == 3
    var_4 = linked_list_0.append(var_1)
    assert len(linked_list_0) == 4
    assert len(var_0.data) == 4
    assert len(var_1.data) == 4
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_3.data) == 4
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'linkedList5.Node'
    assert var_4.next is None
    assert f'{type(var_4.data).__module__}.{type(var_4.data).__qualname__}' == 'linkedList5.Node'
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0

def test_case_3():
    float_0 = -532.81
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.insert_to_front(float_0)
    assert len(linked_list_0) == 2
    assert len(var_0.data) == 2
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert var_1.data == pytest.approx(-532.81, abs=0.01, rel=0.01)
    var_2 = linked_list_0.delete(linked_list_0)
    assert len(linked_list_0) == 1
    assert len(var_0.data) == 1
    assert var_1.next is None

def test_case_4():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 2
    assert len(var_0.data) == 2
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.Node'
    var_2 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 3
    assert len(var_0.data) == 3
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_2.next).__module__}.{type(var_2.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_2.data) == 3
    var_3 = linked_list_0.delete(var_2)
    var_4 = var_2.__str__()
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_4) == 3
    linked_list_1 = module_0.LinkedList(var_2)
    assert len(linked_list_1) == 3

def test_case_5():
    bytes_0 = b'u\x8c\x1c\xf9\xa6\xef>)_\xce\xa6'
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.find(bytes_0)
    var_1 = linked_list_0.print_list()
    var_2 = linked_list_0.print_list()

def test_case_6():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.print_list()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_1.find(var_0)
    var_2 = linked_list_1.print_list()

def test_case_7():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.find(linked_list_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1.data) == 1
    set_0 = {var_0, var_1, linked_list_0}
    var_2 = linked_list_0.append(set_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_0.data) == 2
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_1.data) == 2
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert var_2.next is None
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'builtins.set'
    assert len(var_2.data) == 2
    var_3 = linked_list_0.find(var_1)
    var_4 = var_0.__str__()
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_4) == 2
    var_5 = var_4.delete_alt(var_4)
    var_6 = var_4.__len__()
    assert var_6 == 2
    var_7 = linked_list_0.delete(linked_list_0)
    assert len(linked_list_0) == 1
    assert len(var_0.data) == 1
    assert len(var_1.data) == 1
    assert len(var_4) == 1
    var_8 = linked_list_0.delete_alt(linked_list_0)

def test_case_8():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    list_0 = []
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    linked_list_2 = module_0.LinkedList()
    assert len(linked_list_2) == 0
    var_0 = linked_list_2.__len__()
    assert var_0 == 0

def test_case_9():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    int_0 = -3730
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_0 = linked_list_1.insert_to_front(int_0)
    assert len(linked_list_1) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert var_0.data == -3730
    var_1 = linked_list_1.insert_to_front(linked_list_0)
    assert len(linked_list_1) == 2
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1.data) == 0
    var_2 = linked_list_1.delete_alt(int_0)
    assert len(linked_list_1) == 1
    assert var_1.next is None

def test_case_10():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_0.data) == 2
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1.data) == 2
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_2 = linked_list_0.print_list()
    var_3 = linked_list_0.append(var_1)
    assert len(linked_list_0) == 3
    assert len(var_0.data) == 3
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_1.data) == 3
    assert f'{type(var_3.data).__module__}.{type(var_3.data).__qualname__}' == 'linkedList5.Node'
    var_4 = var_1.__str__()
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_4) == 3
    var_5 = linked_list_1.append(linked_list_1)
    assert len(linked_list_1) == 1
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'linkedList5.Node'
    assert var_5.next is None
    assert f'{type(var_5.data).__module__}.{type(var_5.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_5.data) == 1
    var_6 = var_4.get_all_data()
    var_7 = linked_list_0.delete_alt(var_1)
    assert len(linked_list_0) == 2
    assert len(var_0.data) == 2
    assert var_1.next is None
    assert len(var_1.data) == 2
    assert len(var_4) == 2
    var_8 = linked_list_0.get_all_data()

def test_case_11():
    str_0 = 'qVq(7a'
    none_type_0 = None
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(str_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert var_0.data == 'qVq(7a'
    var_1 = linked_list_0.__len__()
    assert var_1 == 1
    var_2 = linked_list_0.delete(none_type_0)
    var_3 = linked_list_0.insert_to_front(none_type_0)

def test_case_12():
    int_0 = 491
    bool_0 = True
    node_0 = module_0.Node(bool_0)
    linked_list_0 = module_0.LinkedList(int_0)
    none_type_0 = None
    var_0 = linked_list_0.append(none_type_0)
    var_1 = var_0.__str__()
    var_2 = var_1.__len__()
    var_3 = node_0.__str__()
    var_4 = var_2.__str__()

def test_case_13():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete(linked_list_0)
    var_1 = var_0.__str__()
    node_0 = module_0.Node(var_0, linked_list_0)
    assert len(node_0.next) == 0
    node_1 = module_0.Node(var_0)
    none_type_0 = None
    var_2 = linked_list_0.insert_to_front(none_type_0)
    var_3 = linked_list_0.delete_alt(var_2)
    var_4 = node_1.__str__()

def test_case_14():
    none_type_0 = None

def test_case_15():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    node_0 = module_0.Node(linked_list_0)
    assert len(node_0.data) == 0
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_0 = linked_list_1.print_list()
    linked_list_2 = module_0.LinkedList(linked_list_1)
    assert len(linked_list_2.head) == 0
    var_1 = linked_list_1.delete_alt(linked_list_1)
    node_1 = module_0.Node(linked_list_1)
    assert len(node_1.data) == 0
    var_2 = node_1.__str__()
    assert len(var_2) == 0
    var_3 = linked_list_1.print_list()

def test_case_16():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0

def test_case_17():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_0.data) == 2
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1.data) == 2
    var_2 = linked_list_0.delete_alt(var_1)

def test_case_18():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.print_list()
    bool_0 = True
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    dict_0 = {bool_0: linked_list_1, bool_0: linked_list_1}
    node_0 = module_0.Node(dict_0)
    tuple_0 = (bool_0, linked_list_1, dict_0, node_0)
    bool_1 = True
    none_type_0 = None
    node_1 = module_0.Node(none_type_0, none_type_0)
    linked_list_2 = module_0.LinkedList(node_1)
    assert len(linked_list_2) == 1
    var_1 = linked_list_2.delete(bool_1)

def test_case_19():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.find(linked_list_0)
    var_1 = linked_list_0.print_list()
    var_2 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert var_2.next is None
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_2.data) == 1
    var_3 = linked_list_0.print_list()
