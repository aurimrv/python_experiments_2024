import pytest
from binarySearchTree4 import Node, Bst

def test_repr_method():
    # Create a node with data 42
    node = Node(42)

    # Call the __repr__ method
    repr_result = repr(node)

    # Check that the result is a non-empty string
    assert isinstance(repr_result, str)
    assert len(repr_result) > 0

    # Check that the result is the expected string representation of the data
    assert repr_result == "42"

def test_insert_with_none_data():
    # Create a binary search tree
    bst = Bst()

    # Try to insert with None data and expect a TypeError
    with pytest.raises(TypeError, match='data cannot be None'):
        bst.insert(None)

def test_insert_class_method_raises_error():
    # Try to call _insert via the class name without providing the 'data' argument
    try:
        Bst._insert(None, None)
        # If the call didn't raise an exception, fail the test
        assert False, "Expected TypeError, but no exception was raised."
    except TypeError as e:
        # Check that the caught exception has the expected message
        assert str(e) == "Bst._insert() missing 1 required positional argument: 'data'"


