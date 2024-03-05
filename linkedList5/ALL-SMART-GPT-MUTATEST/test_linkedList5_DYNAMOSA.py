#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList5/DYNAMOSA/test_linkedList5.py.orig
import pytest
import linkedList5 as module_0
import builtins as module_1

def test_case_0():
    str_0 = '\txqHl;v&thuBSb3'
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.__len__()
    assert var_1 == 1

def test_case_1():
    none_type_0 = None
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__len__()
    assert var_0 == 0

def test_case_2():
    none_type_0 = None
    linked_list_0 = module_0.LinkedList(none_type_0)
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_1 = linked_list_1.insert_to_front(none_type_0)

def test_case_3():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete_alt(linked_list_0)
    var_1 = var_0.__str__()
    var_2 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert var_2.next is None
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_2.data) == 1
    node_0 = module_0.Node(linked_list_0)
    assert len(node_0.data) == 1

def test_case_4():
    str_0 = '8'
    bool_0 = False
    linked_list_0 = module_0.LinkedList(bool_0)

def test_case_5():
    none_type_0 = None
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.find(none_type_0)

def test_case_6():
    bool_0 = False
    none_type_0 = None
    node_0 = module_0.Node(none_type_0)
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__len__()
    assert var_0 == 0
    var_1 = linked_list_0.find(bool_0)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0

def test_case_7():
    none_type_0 = None
    linked_list_0 = module_0.LinkedList(none_type_0)
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete(none_type_0)
    var_1 = linked_list_0.delete_alt(var_0)
    bool_0 = False
    var_2 = linked_list_0.delete_alt(bool_0)
    bytes_0 = b'\x11'
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_3 = linked_list_1.delete(bytes_0)
    bool_1 = True
    var_4 = linked_list_0.delete_alt(bool_1)
    dict_0 = {}
    var_5 = linked_list_0.delete_alt(dict_0)

def test_case_8():
    bool_0 = True
    bool_1 = True
    set_0 = {bool_1, bool_1, bool_1}
    linked_list_0 = module_0.LinkedList(set_0)

def test_case_9():
    none_type_0 = None
    none_type_1 = None
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete_alt(none_type_1)

def test_case_10():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete_alt(linked_list_0)
    dict_0 = {linked_list_0: linked_list_0, linked_list_0: linked_list_0, linked_list_0: linked_list_0}
    linked_list_1 = module_0.LinkedList(linked_list_0)
    assert len(linked_list_1.head) == 0
    var_1 = linked_list_0.print_list()
    var_2 = linked_list_0.delete(dict_0)
    node_0 = module_0.Node(linked_list_1, linked_list_1)
    var_3 = linked_list_0.__len__()
    assert var_3 == 0

def test_case_11():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = var_0.__str__()
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0

def test_case_12():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0

def test_case_13():
    none_type_0 = None
    node_0 = module_0.Node(none_type_0)
    var_0 = node_0.__str__()
    var_1 = node_0.__str__()
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0

def test_case_14():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.delete_alt(var_1)

def test_case_15():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.print_list()
    var_3 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert var_3.data == []
    var_4 = linked_list_0.delete_alt(var_1)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_5 = linked_list_1.delete(var_4)
    node_0 = module_0.Node(var_0)
    var_6 = linked_list_0.find(var_1)
    linked_list_2 = module_0.LinkedList()
    assert len(linked_list_2) == 0

def test_case_16():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete_alt(linked_list_0)
    dict_0 = {linked_list_0: linked_list_0, linked_list_0: linked_list_0, linked_list_0: linked_list_0}
    linked_list_1 = module_0.LinkedList(linked_list_0)
    assert len(linked_list_1.head) == 0
    var_1 = linked_list_0.delete(dict_0)
    node_0 = module_0.Node(linked_list_1, linked_list_1)
    var_2 = linked_list_0.__len__()
    assert var_2 == 0

def test_case_17():
    tuple_0 = ()
    bool_0 = False
    linked_list_0 = module_0.LinkedList(bool_0)

def test_case_18():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_0.data) == 2
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.Node'

def test_case_19():
    str_0 = 'Ak4e.I$g{AKeN7'
    linked_list_0 = module_0.LinkedList(str_0)

def test_case_20():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_2.next).__module__}.{type(var_2.next).__qualname__}' == 'linkedList5.Node'
    assert var_2.data == []
    var_3 = linked_list_0.delete_alt(var_1)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_4 = linked_list_1.delete(var_3)

def test_case_21():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = module_0.LinkedList()
    assert len(var_1) == 0
    var_2 = module_0.Node(var_1, linked_list_0)
    assert len(var_2.next) == 0
    assert len(var_2.data) == 0
    var_3 = linked_list_0.delete_alt(var_1)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_4 = linked_list_1.delete(var_3)
    linked_list_2 = module_0.LinkedList()
    assert len(linked_list_2) == 0
    var_5 = linked_list_2.insert_to_front(linked_list_2)
    assert len(linked_list_2) == 1
    assert f'{type(var_5).__module__}.{type(var_5).__qualname__}' == 'linkedList5.Node'
    assert var_5.next is None
    assert f'{type(var_5.data).__module__}.{type(var_5.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_5.data) == 1
    var_6 = linked_list_1.delete(var_3)
    node_0 = module_0.Node(var_1)
    assert len(node_0.data) == 0
    var_7 = var_1.__len__()
    assert var_7 == 0
    var_8 = linked_list_2.get_all_data()

def test_case_22():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.print_list()
    var_3 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert var_3.data == []
    var_4 = linked_list_0.delete_alt(var_1)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_5 = linked_list_1.delete(var_4)
    node_0 = module_0.Node(var_0)
    linked_list_2 = module_0.LinkedList()
    assert len(linked_list_2) == 0
    linked_list_3 = module_0.LinkedList(linked_list_0)
    assert len(linked_list_3.head) == 2
    linked_list_4 = module_0.LinkedList()
    assert len(linked_list_4) == 0
    var_6 = linked_list_2.find(linked_list_0)
    var_7 = linked_list_0.__len__()
    assert var_7 == 2
    linked_list_5 = module_0.LinkedList()
    assert len(linked_list_5) == 0

def test_case_23():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.delete_alt(var_0)
    var_3 = linked_list_0.delete_alt(var_1)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_4 = linked_list_1.delete(var_3)
    int_0 = 1394
    var_5 = linked_list_1.find(int_0)

def test_case_24():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.print_list()
    var_3 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert var_3.data == []
    var_4 = linked_list_0.__str__()
    var_5 = linked_list_0.delete_alt(var_1)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_6 = linked_list_1.delete(var_5)
    linked_list_2 = module_0.LinkedList()
    assert len(linked_list_2) == 0
    var_7 = linked_list_2.delete(linked_list_2)
    linked_list_3 = module_0.LinkedList(var_2)
    assert len(linked_list_3) == 0
    linked_list_4 = module_0.LinkedList()
    assert len(linked_list_4) == 0
    var_8 = linked_list_4.get_all_data()
    var_9 = linked_list_2.find(linked_list_0)
    var_10 = linked_list_0.delete_alt(var_9)
    node_0 = module_0.Node(var_9, var_0)
    var_11 = var_6.__str__()
    var_12 = linked_list_4.__str__()
    node_1 = module_0.Node(var_10, var_2)
    var_13 = linked_list_0.__len__()
    assert var_13 == 2
    var_14 = linked_list_0.append(var_11)
    assert len(linked_list_0) == 3
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_14).__module__}.{type(var_14).__qualname__}' == 'linkedList5.Node'
    assert var_14.next is None
    assert var_14.data == 'None'
    var_15 = var_1.__str__()
    var_16 = linked_list_0.get_all_data()

def test_case_25():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.print_list()
    var_3 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert var_3.data == []
    var_4 = linked_list_0.__str__()
    var_5 = linked_list_0.delete_alt(var_1)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    node_0 = module_0.Node(linked_list_0)
    assert len(node_0.data) == 2
    var_6 = linked_list_1.delete(var_5)
    var_7 = linked_list_0.find(var_1)
    var_8 = linked_list_0.delete(linked_list_0)
    linked_list_2 = module_0.LinkedList(var_2)
    assert len(linked_list_2) == 0
    linked_list_3 = module_0.LinkedList()
    assert len(linked_list_3) == 0
    var_9 = linked_list_3.get_all_data()

def test_case_26():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.print_list()
    var_3 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert var_3.data == []
    var_4 = linked_list_0.delete_alt(var_1)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_5 = linked_list_1.delete(var_4)
    var_6 = linked_list_0.find(var_1)
    linked_list_2 = module_0.LinkedList()
    assert len(linked_list_2) == 0
    var_7 = linked_list_0.print_list()
    linked_list_3 = module_0.LinkedList(linked_list_0)
    assert len(linked_list_3.head) == 2
    linked_list_4 = module_0.LinkedList()
    assert len(linked_list_4) == 0
    var_8 = linked_list_2.find(linked_list_0)
    node_0 = module_0.Node(linked_list_3)

def test_case_27():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.print_list()
    var_3 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert var_3.data == []
    var_4 = linked_list_0.delete_alt(var_1)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_5 = linked_list_1.delete(var_4)
    node_0 = module_0.Node(var_0)
    var_6 = linked_list_0.find(var_1)
    var_7 = linked_list_0.find(var_0)
    assert f'{type(var_7).__module__}.{type(var_7).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_7.next).__module__}.{type(var_7.next).__qualname__}' == 'linkedList5.Node'
    assert var_7.data == []
    linked_list_2 = module_0.LinkedList()
    assert len(linked_list_2) == 0
    linked_list_3 = module_0.LinkedList()
    assert len(linked_list_3) == 0
    linked_list_4 = module_0.LinkedList()
    assert len(linked_list_4) == 0
    float_0 = 12.0352

def test_case_28():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.delete(linked_list_0)
    var_2 = linked_list_0.append(var_1)

def test_case_29():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete_alt(linked_list_0)
    dict_0 = {linked_list_0: linked_list_0, linked_list_0: linked_list_0, linked_list_0: linked_list_0}
    linked_list_1 = module_0.LinkedList(linked_list_0)
    assert len(linked_list_1.head) == 0
    var_1 = linked_list_0.delete(dict_0)
    var_2 = linked_list_1.insert_to_front(linked_list_1)
    assert f'{type(linked_list_1.head).__module__}.{type(linked_list_1.head).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_2.next).__module__}.{type(var_2.next).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_2.next) == 0
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.LinkedList'
    node_0 = module_0.Node(linked_list_1, linked_list_1)
    var_3 = linked_list_0.__len__()
    assert var_3 == 0

def test_case_30():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.print_list()
    var_3 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert var_3.data == []
    var_4 = var_0.__str__()
    var_5 = linked_list_0.delete_alt(var_1)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_6 = linked_list_1.delete(var_5)
    var_7 = linked_list_0.find(var_1)
    linked_list_2 = module_0.LinkedList()
    assert len(linked_list_2) == 0
    var_8 = linked_list_2.delete(linked_list_2)
    linked_list_3 = module_0.LinkedList(var_2)
    assert len(linked_list_3) == 0
    linked_list_4 = module_0.LinkedList()
    assert len(linked_list_4) == 0
    var_9 = linked_list_2.find(linked_list_0)
    var_10 = linked_list_0.__len__()
    assert var_10 == 2
    var_11 = linked_list_0.delete_alt(var_9)
    var_12 = var_6.__str__()
    var_13 = var_10.__str__()
    assert var_13 == '2'
    node_0 = module_0.Node(var_11, var_2)
    var_14 = linked_list_0.__len__()
    assert var_14 == 2
    var_15 = linked_list_0.append(var_12)
    assert len(linked_list_0) == 3
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_15).__module__}.{type(var_15).__qualname__}' == 'linkedList5.Node'
    assert var_15.next is None
    assert var_15.data == 'None'
    var_16 = var_1.__str__()

def test_case_31():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.print_list()
    var_2 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert var_2.next is None
    assert var_2.data == []
    var_3 = var_1.__str__()
    var_4 = linked_list_0.delete_alt(linked_list_0)
    var_5 = linked_list_0.delete(var_0)
    assert len(linked_list_0) == 0
    node_0 = module_0.Node(linked_list_0)
    assert len(node_0.data) == 0

def test_case_32():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.append(var_1)
    assert len(linked_list_0) == 2
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert var_2.next is None
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.Node'
    var_3 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 3
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert var_3.data == []
    var_4 = linked_list_0.delete(var_3)
    var_5 = linked_list_0.delete_alt(var_1)
    assert len(linked_list_0) == 2
    assert var_1.next is None
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_6 = linked_list_1.delete(var_5)
    var_7 = linked_list_0.find(var_1)
    linked_list_2 = module_0.LinkedList()
    assert len(linked_list_2) == 0
    var_8 = linked_list_2.delete(linked_list_2)
    linked_list_3 = module_0.LinkedList(var_2)
    assert len(linked_list_3) == 1
    linked_list_4 = module_0.LinkedList()
    assert len(linked_list_4) == 0
    var_9 = linked_list_4.get_all_data()
    var_10 = linked_list_2.find(linked_list_0)

def test_case_33():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = module_1.object()
    var_2 = linked_list_0.print_list()
    var_3 = var_1.__str__()
    var_4 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'linkedList5.Node'
    assert var_4.next is None
    assert var_4.data == []
    var_5 = linked_list_0.delete_alt(var_1)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_6 = linked_list_1.delete(var_5)
    node_0 = module_0.Node(var_0)
    var_7 = linked_list_0.find(var_1)
    linked_list_2 = module_0.LinkedList(linked_list_0)
    assert len(linked_list_2.head) == 1
    var_8 = linked_list_0.delete(var_4)
    linked_list_3 = module_0.LinkedList()
    assert len(linked_list_3) == 0
    linked_list_4 = module_0.LinkedList()
    assert len(linked_list_4) == 0
    var_9 = linked_list_1.find(var_5)

def test_case_34():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()
    var_1 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == []
    var_2 = linked_list_0.print_list()
    var_3 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert var_3.data == []
    var_4 = linked_list_0.__str__()
    var_5 = linked_list_0.delete_alt(var_1)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_6 = linked_list_1.delete(var_5)
    var_7 = linked_list_0.find(var_1)
    linked_list_2 = module_0.LinkedList()
    assert len(linked_list_2) == 0
    var_8 = linked_list_2.delete(linked_list_2)
    linked_list_3 = module_0.LinkedList(var_2)
    assert len(linked_list_3) == 0
    linked_list_4 = module_0.LinkedList()
    assert len(linked_list_4) == 0
    var_9 = linked_list_4.get_all_data()
    var_10 = linked_list_2.find(linked_list_0)
    var_11 = linked_list_0.delete_alt(var_10)
    node_0 = module_0.Node(var_7, var_0)
    assert node_0.data is None
    var_12 = var_6.__str__()
    var_13 = linked_list_4.__str__()
    node_1 = module_0.Node(var_11, var_2)
    var_14 = linked_list_0.__len__()
    assert var_14 == 2
    var_15 = linked_list_0.append(var_12)
    assert len(linked_list_0) == 3
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_15).__module__}.{type(var_15).__qualname__}' == 'linkedList5.Node'
    assert var_15.next is None
    assert var_15.data == 'None'
    var_16 = linked_list_0.append(linked_list_4)
    assert len(linked_list_0) == 4
    assert f'{type(var_15.next).__module__}.{type(var_15.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_16).__module__}.{type(var_16).__qualname__}' == 'linkedList5.Node'
    assert var_16.next is None
    assert f'{type(var_16.data).__module__}.{type(var_16.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_16.data) == 0
    var_17 = var_11.__str__()
    linked_list_5 = module_0.LinkedList(var_2)
    assert len(linked_list_5) == 0
    var_18 = linked_list_5.append(var_17)
    assert len(linked_list_5) == 1
    assert f'{type(var_18).__module__}.{type(var_18).__qualname__}' == 'linkedList5.Node'
    assert var_18.next is None
    assert var_18.data == 'None'

def test_case_35():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.print_list()
    var_2 = linked_list_0.insert_to_front(var_0)
    assert len(linked_list_0) == 2
    assert len(var_0.data) == 2
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_2.next).__module__}.{type(var_2.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.Node'
    var_3 = linked_list_0.delete(var_2)
    var_4 = linked_list_0.delete_alt(var_0)
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    linked_list_2 = module_0.LinkedList()
    assert len(linked_list_2) == 0
    var_5 = linked_list_0.delete(linked_list_0)
    assert len(linked_list_0) == 1
    assert len(var_0.data) == 1
    assert var_2.next is None
