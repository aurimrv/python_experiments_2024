#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList5/MIO/test_linkedList5.py.orig
import pytest
import linkedList5 as module_0

def test_case_0():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
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
    var_2 = linked_list_0.__len__()
    assert var_2 == 2

def test_case_1():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete(linked_list_0)
    var_1 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1.data) == 1
    var_2 = linked_list_0.__len__()
    assert var_2 == 1

def test_case_2():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.__len__()
    assert var_0 == 0

def test_case_3():
    none_type_0 = None
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(none_type_0)

def test_case_4():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1

def test_case_5():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1

def test_case_6():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
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

def test_case_7():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
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
    var_2 = linked_list_0.append(var_1)
    assert len(linked_list_0) == 3
    assert len(var_0.data) == 3
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert var_2.next is None
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.Node'
    var_3 = linked_list_0.delete_alt(var_1)
    assert len(linked_list_0) == 2
    assert len(var_0.data) == 2
    assert var_1.next is None

def test_case_8():
    bool_0 = True
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    linked_list_1 = module_0.LinkedList(linked_list_0)
    assert len(linked_list_1.head) == 1
    var_1 = linked_list_0.find(linked_list_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1.data) == 1
    var_2 = linked_list_0.append(bool_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_0.data) == 2
    assert len(linked_list_1.head) == 2
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert len(var_1.data) == 2
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert var_2.next is None
    assert var_2.data is True
    var_3 = linked_list_0.insert_to_front(bool_0)
    assert len(linked_list_0) == 3
    assert len(var_0.data) == 3
    assert len(linked_list_1.head) == 3
    assert len(var_1.data) == 3
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3.next).__module__}.{type(var_3.next).__qualname__}' == 'linkedList5.Node'
    assert var_3.data is True
    var_4 = linked_list_0.append(var_1)
    assert len(linked_list_0) == 4
    assert len(var_0.data) == 4
    assert len(linked_list_1.head) == 4
    assert len(var_1.data) == 4
    assert f'{type(var_2.next).__module__}.{type(var_2.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_4).__module__}.{type(var_4).__qualname__}' == 'linkedList5.Node'
    assert var_4.next is None
    assert f'{type(var_4.data).__module__}.{type(var_4.data).__qualname__}' == 'linkedList5.Node'

def test_case_9():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    none_type_0 = None
    var_0 = linked_list_0.append(none_type_0)

def test_case_10():
    str_0 = "fW#DXl1'J"
    linked_list_0 = module_0.LinkedList(str_0)

def test_case_11():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.find(linked_list_0)

def test_case_12():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
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
    var_2 = linked_list_0.find(var_0)
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert var_2.next is None
    assert f'{type(var_2.data).__module__}.{type(var_2.data).__qualname__}' == 'linkedList5.Node'

def test_case_13():
    dict_0 = {}
    tuple_0 = (dict_0, dict_0)
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(dict_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert var_0.data == {}
    var_1 = linked_list_0.find(linked_list_0)
    var_2 = linked_list_0.append(dict_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_2).__module__}.{type(var_2).__qualname__}' == 'linkedList5.Node'
    assert var_2.next is None
    assert var_2.data == {}
    var_3 = linked_list_0.delete_alt(var_2)

def test_case_14():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    none_type_0 = None
    var_0 = linked_list_0.find(none_type_0)

def test_case_15():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete(linked_list_0)

def test_case_16():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.delete(var_0)

def test_case_17():
    int_0 = -3408
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(int_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert var_0.data == -3408
    var_1 = linked_list_0.delete(int_0)
    assert len(linked_list_0) == 0

def test_case_18():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
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
    var_2 = linked_list_0.delete(var_1)

def test_case_19():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
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
    var_2 = linked_list_0.delete(var_0)
    assert len(linked_list_0) == 1
    assert var_0.next is None
    assert len(var_0.data) == 1
    var_3 = linked_list_0.delete_alt(var_1)

def test_case_20():
    int_0 = -363
    set_0 = {int_0, int_0, int_0, int_0}
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(set_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert var_0.data == {-363}
    var_1 = linked_list_0.append(set_0)
    assert len(linked_list_0) == 2
    assert f'{type(var_0.next).__module__}.{type(var_0.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.Node'
    assert var_1.next is None
    assert var_1.data == {-363}
    linked_list_1 = module_0.LinkedList()
    assert len(linked_list_1) == 0
    var_2 = linked_list_0.delete_alt(linked_list_0)
    node_0 = module_0.Node(linked_list_1)
    assert len(node_0.data) == 0
    var_3 = linked_list_0.append(var_0)
    assert len(linked_list_0) == 3
    assert f'{type(var_1.next).__module__}.{type(var_1.next).__qualname__}' == 'linkedList5.Node'
    assert f'{type(var_3).__module__}.{type(var_3).__qualname__}' == 'linkedList5.Node'
    assert var_3.next is None
    assert f'{type(var_3.data).__module__}.{type(var_3.data).__qualname__}' == 'linkedList5.Node'
    var_4 = linked_list_0.delete(var_3)
    node_1 = module_0.Node(var_2)
    var_5 = linked_list_1.find(var_1)

def test_case_21():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.find(linked_list_0)
    var_1 = linked_list_0.delete(var_0)

def test_case_22():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete_alt(linked_list_0)

def test_case_23():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.delete_alt(linked_list_0)

def test_case_24():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.append(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.delete_alt(var_0)

def test_case_25():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
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
    var_2 = linked_list_0.delete_alt(var_1)

def test_case_26():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.delete(linked_list_0)
    var_1 = linked_list_0.delete_alt(var_0)

def test_case_27():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
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

def test_case_28():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = var_0.__str__()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1) == 1
    var_2 = var_1.print_list()

def test_case_29():
    bool_0 = True
    linked_list_0 = module_0.LinkedList(bool_0)

def test_case_30():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.print_list()

def test_case_31():
    bool_0 = False
    node_0 = module_0.Node(bool_0, bool_0)
    linked_list_0 = module_0.LinkedList(node_0)

def test_case_32():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = linked_list_0.get_all_data()
    var_2 = linked_list_0.delete_alt(var_0)

def test_case_33():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.get_all_data()

def test_case_34():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0

def test_case_35():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    node_0 = module_0.Node(linked_list_0, linked_list_0)
    assert len(node_0.next) == 0
    assert len(node_0.data) == 0

def test_case_36():
    linked_list_0 = module_0.LinkedList()
    assert len(linked_list_0) == 0
    var_0 = linked_list_0.insert_to_front(linked_list_0)
    assert len(linked_list_0) == 1
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList5.Node'
    assert var_0.next is None
    assert f'{type(var_0.data).__module__}.{type(var_0.data).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_0.data) == 1
    var_1 = var_0.__str__()
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList5.LinkedList'
    assert len(var_1) == 1
