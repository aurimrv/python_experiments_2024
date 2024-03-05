import pytest
from queue5 import Queue, Node

def test_node_creation():
    # Create a node
    node = Node(42)

    # Verify that the data attribute is set correctly
    assert node.data == 42

    # Verify that the next attribute is None
    assert node.next is None
