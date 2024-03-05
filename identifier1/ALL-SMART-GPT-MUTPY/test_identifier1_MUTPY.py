import pytest
from identifier1 import Identifier


def test_call_valids():
    with pytest.raises(TypeError) as typeerror:
        identifier = Identifier.valid_s('a')

def test_call_validf():
    with pytest.raises(TypeError) as typeerror:
        identifier = Identifier.valid_f('a')

def test_edge_cases():
    identifier_instance = Identifier()

    assert identifier_instance.valid_s('a') == True

    assert identifier_instance.valid_s('z') == True

    assert identifier_instance.valid_s('A') == True

    assert identifier_instance.valid_s('Z') == True

    assert identifier_instance.valid_f('A') == True
    
    assert identifier_instance.valid_f('Z') == True

    assert identifier_instance.valid_f('a') == True

    assert identifier_instance.valid_f('0') == True

def test_validate_identifier_max_length():
    identifier_instance = Identifier()
    
    assert identifier_instance.validateIdentifier('AbCdEf') == True

def test_valid_f_special_char():
    identifier_instance = Identifier()
    
    assert identifier_instance.valid_f('$') == False

def test_valid_s_special_char():
    identifier_instance = Identifier()
    
    assert identifier_instance.valid_s('[') == False
