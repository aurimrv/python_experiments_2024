#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/linkedList4/MIO/test_linkedList4.py.orig
import pytest
import linkedList4 as module_0

def test_case_0():
    bytes_0 = b'\x97'
    linked_list_0 = module_0.LinkedList(bytes_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'

def test_case_1():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    linked_list_1 = module_0.LinkedList(linked_list_0)
    assert f'{type(linked_list_1.head).__module__}.{type(linked_list_1.head).__qualname__}' == 'linkedList4.Node'

def test_case_2():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None

def test_case_3():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    linked_list_1 = module_0.LinkedList(linked_list_0)
    assert f'{type(linked_list_1.head).__module__}.{type(linked_list_1.head).__qualname__}' == 'linkedList4.Node'
    var_0 = linked_list_1.pop()
    assert linked_list_1.head is None
    assert f'{type(var_0).__module__}.{type(var_0).__qualname__}' == 'linkedList4.LinkedList'
    assert var_0.head is None

def test_case_4():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    with pytest.raises(IndexError):
        linked_list_0.pop()

def test_case_5():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.search(linked_list_0)
    assert f'{type(var_1).__module__}.{type(var_1).__qualname__}' == 'linkedList4.Node'
    assert f'{type(var_1.data).__module__}.{type(var_1.data).__qualname__}' == 'linkedList4.LinkedList'
    assert var_1.next is None

def test_case_6():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.search(var_0)

def test_case_7():
    str_0 = "\x0c_|J;I>6~W4+\x0b'A(3"
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'
    var_0 = linked_list_0.search(str_0)

def test_case_8():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.search(linked_list_0)

def test_case_9():
    str_0 = 'qfpV75uhWnpJp\nJ]qxP'
    linked_list_0 = module_0.LinkedList(str_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'
    var_0 = linked_list_0.remove(str_0)

def test_case_10():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.remove(linked_list_0)
    assert linked_list_0.head is None

def test_case_11():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.remove(var_0)

def test_case_12():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.remove(linked_list_0)

def test_case_13():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.push(linked_list_0)
    var_2 = linked_list_0.remove(linked_list_0)

def test_case_14():
    bytes_0 = b'\t\xc8 \xcf\xb9\x96\x93\xba\x88\x1f\xa0{\xba\xab\xc2\xeb\xc1;\xff'
    linked_list_0 = module_0.LinkedList(bytes_0)
    assert f'{type(linked_list_0.head).__module__}.{type(linked_list_0.head).__qualname__}' == 'linkedList4.Node'
    var_0 = linked_list_0.display()
    assert var_0 == '(255, 59, 193, 235, 194, 171, 186, 123, 160, 31, 136, 186, 147, 150, 185, 207, 32, 200, 9)'

def test_case_15():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.push(linked_list_0)
    var_1 = linked_list_0.display()

def test_case_16():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.display()
    assert var_0 == ')'

def test_case_17():
    linked_list_0 = module_0.LinkedList()
    assert f'{type(linked_list_0).__module__}.{type(linked_list_0).__qualname__}' == 'linkedList4.LinkedList'
    assert linked_list_0.head is None
    var_0 = linked_list_0.size()
    assert var_0 == 0
