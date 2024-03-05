import pytest
from stack4 import LinkedList, Stack 

def test_linked_list_push_pop():
    # Test the push and pop methods of LinkedList
    linked_list = LinkedList()

    linked_list.push(10)
    assert linked_list.pop() == 10

def test_linked_list_size():
    # Test the size method of LinkedList
    linked_list = LinkedList()

    assert linked_list.size() == 0

def test_linked_list_search():
    # Test the search method of LinkedList
    linked_list = LinkedList([10, 20, 30, 40, 50])

    assert linked_list.search(30).data == 30

def test_linked_list_remove():
    # Test the remove method of LinkedList
    linked_list = LinkedList([10, 20, 30, 40, 50])

    linked_list.remove(30)
    assert linked_list.size() == 4

def test_stack_exception():
    # Test that attempting to pop from an empty stack raises an exception
    stack = Stack()

    with pytest.raises(IndexError, match='Cannot pop from an empty list'):
        stack.pop()

def test_linked_list_pop():
    # Test the pop method of LinkedList
    linked_list = LinkedList([10, 20, 30])

    # Test popping an element from a non-empty list
    popped_value = linked_list.pop()
    assert linked_list.size() == 2

def test_linked_list_remove_length():
    # Test the remove method of LinkedList affecting the length
    linked_list = LinkedList([10, 20, 30, 40, 50])

    # Before removing any node, the length should be the initial size of the list
    initial_length = linked_list.size()

    # Remove a node from the list
    linked_list.remove(50)

    # After removing a node, the length should be reduced by 1
    assert linked_list.size() == initial_length - 1

def test_call_init():
    with pytest.raises(TypeError) as typeerror:
        stack = Stack.__init__()

def test_remove_from_linked_list():
    data = ['apple', 'banana', 'cherry', 'date']
    linked_list = LinkedList(data)

    # Test initial state
    assert linked_list.size() == 4
    assert linked_list.display() == "(date, cherry, banana, apple)"

    # Remove the 3rd element ('cherry')
    linked_list.remove('cherry')

    # Test after removal
    assert linked_list.size() == 3
    assert linked_list.display() == "(date, banana, apple)"
