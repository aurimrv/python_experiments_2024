import unittest
import sys
import os

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        myPath = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, myPath + '/../')

        from linkedList4 import LinkedList, Node
        self.empty = LinkedList()
        self.one = LinkedList(5)
        self.multi = LinkedList([1, 2, 3, 4, 5])
        self.ll = Node(5)

    def test_node_has_data(self):
        """Test node object has data."""
        self.assertEqual(self.ll.data, 5)
        self.assertIsNone(self.ll.next)

    def test_push_adds_to_the_head(self):
        """Test push, adds to the head of the list."""
        self.assertEqual(self.one.head.data, 5)

    def test_ll_has_head(self):
        """Test ll with iterable has a head."""
        self.assertEqual(self.multi.head.data, 5)

    def test_empty_ll_head_none(self):
        """Test empty ll has a head of None."""
        self.assertIsNone(self.empty.head)

    def test_size_one(self):
        """Test ll of one has length of one."""
        self.assertEqual(self.one._length, 1)

    def test_length_multi(self):
        """Test ll of multi has length."""
        self.assertEqual(self.multi._length, 5)

    def test_empty_list_length(self):
        """Test empty list has no length."""
        self.assertEqual(self.empty._length, 0)

    def test_when_push_increases_length(self):
        """Test push increases length."""
        ll = self.one
        length = ll._length
        ll.push(3)
        self.assertEqual(ll._length, length + 1)

    def test_pop_multi_list(self):
        """Test pop on list of 5."""
        ll = self.multi
        ll.pop()
        self.assertEqual(ll.head.data, 4)

    def test_pop_returns_data(self):
        """Test pop method returns data of removed node."""
        returned = self.multi.pop()
        self.assertEqual(returned, 5)

    def test_pop_decreases_length(self):
        """Test pop decreases length."""
        ll = self.multi
        length = ll._length
        ll.pop()
        self.assertEqual(ll._length, length - 1)

    def test_pop_list_one(self):
        """Test pop on list of one."""
        self.one.pop()
        self.assertIsNone(self.one.head)

    def test_pop_decreases_length_to_zero(self):
        ll = self.one
        length = ll._length
        ll.pop()
        self.assertEqual(ll._length, length - 1)

    def test_cant_pop_on_empty_list(self):
        with self.assertRaises(IndexError):
            self.empty.pop()

    def test_size_function(self):
        self.assertEqual(self.empty.size(), 0)

    def test_size_function_list(self):
        self.assertEqual(self.multi.size(), 5)

    def test_size_after_push(self):
        ll = self.empty
        length = ll.size()
        ll.push(4)
        self.assertEqual(ll.size(), length + 1)

    def test_size_after_pop(self):
        ll = self.multi
        length = ll.size()
        ll.pop()
        self.assertEqual(ll.size(), length - 1)

    def test_size_after_push_and_pop(self):
        ll = self.multi
        ll.push(4)
        ll.push(2)
        ll.pop()
        self.assertEqual(ll.size(), 6)

    def test_search_on_list(self):
        self.assertEqual(self.multi.search(2).data, 2)

    def test_search_on_list_no_value(self):
        self.assertEqual(self.multi.search(9), None)

    def test_remove_on_list(self):
        self.multi.remove(4)
        self.assertEqual(self.multi.size(), 4)

    def test_remove_second_end_of_list(self):
        self.multi.remove(2)
        self.assertEqual(self.multi.size(), 4)

    def test_remove_on_end_of_list(self):
        self.multi.remove(1)
        self.assertEqual(self.multi.size(), 4)

    def test_remove_on_list_with_no_node(self):
        self.multi.remove(9)
        self.assertEqual(self.multi.size(), 5)

    def test_remove_on_empty_list(self):
        self.empty.remove(1)
        self.assertEqual(self.empty.size(), 0)

    def test_remove_on_list_one_list(self):
        """Test remove from list of 1."""
        self.one.remove(5)
        self.assertEqual(self.one.size(), 0)

    def test_remove_on_start_of_list(self):
        """Test remove start node in list."""
        self.multi.remove(5)
        self.assertEqual(self.multi.size(), 4)

    def test_display_method(self):
        """Test display method."""
        self.assertEqual(self.multi.display(), '(5, 4, 3, 2, 1)')

    def test_display_method_one(self):
        """Test display method."""
        self.assertEqual(self.one.display(), '(5)')

if __name__ == '__main__':
    unittest.main()
