#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/sort1/MIO/test_sort1.py.orig
import pytest
import sort1 as module_0

def test_case_0():
    bytes_0 = b'\x80\xe0\xa6_\x8b'
    sort_0 = module_0.Sort()

def test_case_1():
    bytes_0 = b''
    sort_0 = module_0.Sort()
    var_0 = sort_0.selection_sort(bytes_0)
    assert var_0 == b''

def test_case_2():
    sort_0 = module_0.Sort()
    list_0 = [sort_0, sort_0]

def test_case_3():
    sort_0 = module_0.Sort()
    str_0 = 'P'

def test_case_4():
    bytes_0 = b'\x9b.\xf1h|'
    sort_0 = module_0.Sort()
    var_0 = sort_0.merge(bytes_0, bytes_0)
    var_1 = sort_0.insertion_sort(var_0)
    sort_1 = module_0.Sort()

def test_case_5():
    list_0 = []
    sort_0 = module_0.Sort()
    var_0 = sort_0.insertion_sort(list_0)

def test_case_6():
    int_0 = -1168
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0, int_0]
    sort_0 = module_0.Sort()
    var_0 = sort_0.insertion_sort(list_0)

def test_case_7():
    bytes_0 = b'\xca\xb5\xa1?L\x0f+3v'
    sort_0 = module_0.Sort()
    var_0 = sort_0.merge_sort(bytes_0)

def test_case_8():
    bytes_0 = b'\xcd{7\xc3\xe7\x9fM\x9c\xa4\x12\xa3\xc5-\xc1}\x91\xe1\x15\xde'
    dict_0 = {}
    sort_0 = module_0.Sort()
    var_0 = sort_0.merge(bytes_0, dict_0)

def test_case_9():
    sort_0 = module_0.Sort()
    list_0 = []

def test_case_10():
    sort_0 = module_0.Sort()
    list_0 = []
    var_0 = sort_0.merge(list_0, list_0)

def test_case_11():
    int_0 = 1020
    bool_0 = False
    sort_0 = module_0.Sort()

def test_case_12():
    bool_0 = False
    sort_0 = module_0.Sort()
    var_0 = sort_0.quick_sort(sort_0, bool_0, bool_0)

def test_case_13():
    bytes_0 = b'\xa8\xea\t\xd2\x96\x82\x88\x8e\xb0-b;\xa7\x80'
    bool_0 = False
    bool_1 = True
    sort_0 = module_0.Sort()

def test_case_14():
    bytes_0 = b'\xca\xb5\xa1?L\x0f+3v'
    bool_0 = False
    bool_1 = True
    sort_0 = module_0.Sort()

def test_case_15():
    bool_0 = True
    sort_0 = module_0.Sort()
    bool_1 = False

def test_case_16():
    bool_0 = True
    sort_0 = module_0.Sort()

def test_case_17():
    sort_0 = module_0.Sort()
