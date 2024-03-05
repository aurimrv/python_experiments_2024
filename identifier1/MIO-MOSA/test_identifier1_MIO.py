#Pyguin test cases converted from /home/auri/temp/lucca/python_experiments/identifier1/MIO/test_identifier1.py.orig
import identifier1 as module_0

def test_case_0():
    str_0 = 'e=g'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False

def test_case_1():
    str_0 = ''
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.valid_s(str_0)
    assert var_0 is False

def test_case_2():
    str_0 = 'M'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is True

def test_case_3():
    str_0 = '}\t'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.valid_s(str_0)
    assert var_0 is False

def test_case_4():
    str_0 = 'y'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.valid_f(str_0)
    assert var_0 is True

def test_case_5():
    str_0 = 'S\x0c'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False

def test_case_6():
    identifier_0 = module_0.Identifier()
    str_0 = 'HI8ft5A\x0bj%%;.q.1@'
    var_0 = identifier_0.valid_f(str_0)
    assert var_0 is True

def test_case_7():
    str_0 = 'uW\t}a5Qe+4i#yaFe'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False

def test_case_8():
    str_0 = 'cqVsCRHL'
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False

def test_case_9():
    str_0 = ''
    identifier_0 = module_0.Identifier()
    var_0 = identifier_0.validateIdentifier(str_0)
    assert var_0 is False

def test_case_10():
    identifier_0 = module_0.Identifier()
