#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/identifier1/DYNAMOSA/test_identifier1.py.orig
import pytest
import identifier1 as module_0

def test_case_0():
    str_0 = 'i8'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is True

def test_case_1():
    str_0 = 'ij'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is True

def test_case_2():
    identifier_0 = module_0.Identifier()

def test_case_3():
    str_0 = 'K^'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False

def test_case_4():
    str_0 = '!W'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False

def test_case_5():
    str_0 = 't'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is True

def test_case_6():
    str_0 = "w'"
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False

def test_case_7():
    str_0 = 'i8='
    str_1 = 'j'
    dict_0 = {}
    identifier_0 = module_0.Identifier(**dict_0)
    var_0 = identifier_0.validateIdentifier(str_1)
    assert var_0 is True
    var_1 = identifier_0.validateIdentifier(str_0)
    assert var_1 is False

def test_case_8():
    str_0 = 'Y'
    list_0 = []
    identifier_0 = module_0.Identifier(*list_0)
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is True
    var_1 = identifier_0.validateIdentifier(list_0)
    assert var_1 is False

def test_case_9():
    str_0 = '/C@||M'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False
    identifier_1 = module_0.Identifier()

def test_case_10():
    str_0 = '}'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False

def test_case_11():
    str_0 = 'F5Rb7vOq'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False
    int_0 = -3745
    identifier_1 = module_0.Identifier()
