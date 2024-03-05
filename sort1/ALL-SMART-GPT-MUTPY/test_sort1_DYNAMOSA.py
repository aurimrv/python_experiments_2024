#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/sort1/DYNAMOSA/test_sort1.py.orig
import pytest
import sort1 as module_0

def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    sort_0 = module_0.Sort()
    var_0 = sort_0.insertion_sort(list_0)
    var_1 = sort_0.partition(var_0, bool_0, bool_0)
    assert var_1 is False
    var_2 = sort_0.selection_sort(var_0)
    complex_0 = -1296 + 1520.3j

def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    sort_0 = module_0.Sort()
    var_0 = sort_0.insertion_sort(list_0)

def test_case_2():
    sort_0 = module_0.Sort()
    str_0 = 'Z^[`[*-KJ8P&'
    dict_0 = sort_0.merge_sort(str_0)

def test_case_3():
    bool_0 = False
    sort_0 = module_0.Sort()

def test_case_4():
    list_0 = []
    sort_0 = module_0.Sort(*list_0)

def test_case_5():
    bytes_0 = b'\x1d\xb6\x17\xd9e\xf0?v'
    sort_0 = module_0.Sort()

def test_case_6():
    str_0 = 'bw\r'
    sort_0 = module_0.Sort()
    var_0 = sort_0.quick_sort(str_0, str_0, str_0)

def test_case_7():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    sort_0 = module_0.Sort()
    var_0 = sort_0.insertion_sort(list_0)
    dict_0 = {}
    var_1 = sort_0.selection_sort(dict_0)
    var_2 = sort_0.merge(var_1, var_1)
    sort_1 = module_0.Sort(**dict_0)
    var_3 = sort_0.selection_sort(list_0)
    sort_2 = module_0.Sort()
    var_4 = sort_2.merge_sort(var_0)
    var_5 = sort_2.insertion_sort(var_3)

def test_case_8():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    sort_0 = module_0.Sort()
    var_0 = sort_0.insertion_sort(list_0)
    str_0 = 'Z^[`[*-KJ8P&'
    dict_0 = {}
    var_1 = sort_0.merge(var_0, dict_0)

def test_case_9():
    bool_0 = False
    bool_1 = True
    sort_0 = module_0.Sort()

def test_case_10():
    bool_0 = False
    sort_0 = module_0.Sort()
    str_0 = 'Z^[`[*-KJ8P&'
    bool_1 = True

def test_case_11():
    bool_0 = False
    sort_0 = module_0.Sort()
    str_0 = 'C>Y4MFo<2vL.Hb'
    bool_1 = True

def test_case_12():
    bool_0 = True
    float_0 = -491.8264
    list_0 = [bool_0, float_0]
    sort_0 = module_0.Sort()
    var_0 = sort_0.insertion_sort(list_0)

def test_case_13():
    bool_0 = False
    float_0 = -487.3549775499703
    list_0 = [bool_0, bool_0, float_0]
    sort_0 = module_0.Sort()
    var_0 = sort_0.insertion_sort(list_0)

def test_case_14():
    bool_0 = False
    float_0 = -487.3549775499703
    list_0 = [float_0, bool_0, bool_0, bool_0, float_0, float_0]
    sort_0 = module_0.Sort()
    var_0 = sort_0.insertion_sort(list_0)
