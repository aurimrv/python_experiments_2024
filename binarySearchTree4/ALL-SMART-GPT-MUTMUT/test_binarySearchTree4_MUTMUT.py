import pytest
from binarySearchTree4 import Node, Bst

def test_insert_with_none_data():
    # Create a binary search tree
    bst = Bst()

    with pytest.raises(Exception) as exception:
        bst.insert(None)
    assert str(exception.value) == "data cannot be None"
