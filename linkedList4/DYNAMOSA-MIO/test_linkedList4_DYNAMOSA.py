#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList4/DYNAMOSA/test_linkedList4.py.orig
import pytest
import linkedList4 as module_0

def test_case_0():
    bool_0 = True
    str_0 = 'r*tmGzmF T'
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'
    var_0 = linked_list_0.search(bool_0)

def test_case_1():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None

def test_case_2():
    list_0 = []
    bool_0 = True
    linked_list_0 = module_0.LinkedList(bool_0)
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'
    var_0 = linked_list_0.pop()
    assert var_0 is True
    assert linked_list_0.head is None

def test_case_3():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    with pytest.raises(IndexError):
        linked_list_0.pop()

def test_case_4():
    list_0 = []
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.search(list_0)
    node_0 = module_0.Node(linked_list_0)

def test_case_5():
    set_0 = set()
    str_0 = 'rF,-'
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.remove(str_0)

def test_case_6():
    bytes_0 = b'\x1a8\xa3\x01x\x91\xc6'
    linked_list_0 = module_0.LinkedList(bytes_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'
    var_0 = linked_list_0.display()
    assert var_0 == '(198, 145, 120, 1, 163, 56, 26)'

def test_case_7():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    node_0 = module_0.Node(linked_list_0)
    linked_list_1 = module_0.LinkedList()
    assert linked_list_1.head is None
    complex_0 = -1718.4 - 1928.75728j
    var_0 = linked_list_0.remove(complex_0)
    var_1 = linked_list_1.display()
    assert var_1 == ')'
    var_2 = linked_list_1.display()
    assert var_2 == ')'

def test_case_8():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.size()
    assert var_0 == 0

def test_case_9():
    int_0 = -1014
    linked_list_0 = module_0.LinkedList(int_0)
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'
    var_0 = linked_list_0.search(int_0)
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList4.Node'
    assert var_0.data == -1014
    assert var_0.next is None

def test_case_10():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    node_0 = linked_list_0.push(linked_list_0)
    linked_list_1 = module_0.LinkedList()
    assert linked_list_1.head is None
    complex_0 = -1718.4 - 1928.75728j
    var_0 = linked_list_0.remove(complex_0)
    var_1 = linked_list_1.display()
    assert var_1 == ')'
    linked_list_2 = module_0.LinkedList()
    assert linked_list_2.head is None

def test_case_11():
    bytes_0 = b'\xeb~\xd3\xf1\x97S['
    linked_list_0 = module_0.LinkedList(bytes_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'
    str_0 = 'Hf.;eT9\rj|uBvm'
    var_0 = linked_list_0.remove(str_0)
    node_0 = module_0.Node(linked_list_0)
    linked_list_1 = module_0.LinkedList()
    assert f'{type(linked_list_1).__module__}.{type(linked_list_1).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_1.head is None
    with pytest.raises(IndexError):
        linked_list_1.pop()

def test_case_12():
    complex_0 = 4727.02 - 1515.24033j
    linked_list_0 = module_0.LinkedList(complex_0)
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'
    var_0 = linked_list_0.remove(complex_0)
    assert linked_list_0.head is None
    bool_0 = False
    node_0 = module_0.Node(bool_0)
    linked_list_1 = module_0.LinkedList()
    assert linked_list_1.head is None

def test_case_13():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    bool_0 = False
    linked_list_1 = module_0.LinkedList(bool_0)
    assert linked_list_1.head is None
    linked_list_2 = module_0.LinkedList()
    assert linked_list_2.head is None
    var_0 = linked_list_2.push(linked_list_2)
    var_1 = linked_list_2.push(var_0)
    var_2 = linked_list_2.remove(linked_list_2)
    linked_list_3 = module_0.LinkedList()
    assert linked_list_3.head is None
    with pytest.raises(IndexError):
        linked_list_1.pop()
