import unittest
from binarySearchTree3 import Bst

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.empty = Bst()
        self.one = Bst([5])
        self.three = Bst([5, 3, 7])
        self.balance = Bst([5, 3, 2, 4, 9, 7, 10])
        self.leftheavy = Bst([5, 3, 2, 1])
        self.rightheavy = Bst([5, 6, 7, 8, 9, 10])
        self.fixture = {
            'tree': Bst(['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']),
            'empty': Bst(),
            'pre_order': ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H'],
            'in_order': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            'post_order': ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F'],
            'breadth': ['F', 'B', 'G', 'A', 'D', 'I', 'C', 'E', 'H']
        }
        
    def test_node_is_leaf(self):
        self.assertTrue(self.one.root._is_leaf())

    def test_insert_sets_root(self):
        self.empty.insert(5)
        self.assertEqual(self.empty.root.val, 5)

    def test_insert_updates_pointers(self):
        self.one.insert(3)
        self.assertEqual(self.one.root.left.val, 3)
        self.assertEqual(self.one.root.left.parent, self.one.root)

    def test_insert_smallest_left(self):
        self.one.insert(3)
        self.assertTrue(self.one.root.left.val < self.one.root.val)

    def test_insert_largest_right(self):
        self.one.insert(7)
        self.assertTrue(self.one.root.right.val > self.one.root.val)

    def test_insert_increases_size(self):
        self.empty.insert(4)
        self.assertEqual(self.empty.size(), 1)

    def test_contains_method(self):
        self.assertTrue(self.three.contains(5))
        self.assertTrue(self.three.contains(3))
        self.assertTrue(self.three.contains(7))

    def test_contains_method_no_val(self):
        self.assertFalse(self.leftheavy.contains(10))

    def test_depth_method(self):
        """Test depth method."""
        depths = [0, 1, 2, 3, 4, 6]
        self.assertTrue(all(tree.depth() == depths[idx]
               for idx, tree in enumerate([self.empty, self.one, self.three, self.balance, self.leftheavy, self.rightheavy])))

    def test_balance_method(self):
        """Test the balance method."""
        balance = [0, 0, 0, 0, 3, -5]
        self.assertTrue(all(tree.balance() == balance[idx]
               for idx, tree in enumerate([self.empty, self.one, self.three, self.balance, self.leftheavy, self.rightheavy])))

    def test_search_method_node_exists(self):
        """Test search method for a node that exists."""
        self.assertTrue(all(tree.search(5) for tree in [self.one, self.three, self.balance, self.leftheavy, self.rightheavy]))

    def test_pre_order(self):
        """Test preorder for a traversal."""
        path = [i for i in self.fixture['tree'].pre_order()]
        self.assertEqual(path, self.fixture['pre_order'])

    def test_in_order(self):
        """Test inorder for a traversal."""
        path = [i for i in self.fixture['tree'].in_order()]
        self.assertEqual(path, self.fixture['in_order'])

    def test_post_order(self):
        path = [i for i in self.fixture['tree'].post_order()]
        self.assertEqual(path, self.fixture['post_order'])

    def test_breadth_first(self):
        path = [i for i in self.fixture['tree'].breadth_first()]
        self.assertEqual(path, self.fixture['breadth'])

    def test_traversals_none(self):
        path = [i for i in self.fixture['empty'].in_order()]
        self.assertEqual(path, [])

    def test_del_false(self):
        size = self.three.size()
        self.three.delete(1)
        self.assertEqual(self.three.size(), size)

    def test_del_empty_tree(self):
        self.empty.delete(1)
        self.assertEqual(self.empty.size(), 0)

    def test_remove_leaf_left(self):
        self.three.delete(3)
        self.assertFalse(self.three.contains(3))
        self.assertEqual(self.three.size(), 2)

    def test_remove_leaf_right(self):
        self.three.delete(7)
        self.assertFalse(self.three.contains(7))
        self.assertEqual(self.three.size(), 2)

    def test_remove_leaf_root(self):
        self.one.delete(5)
        self.assertFalse(self.one.contains(5))
        self.assertEqual(self.one.size(), 0)

    def test_remove_one_child_left(self):
        """Test delete node one child, left."""
        self.leftheavy.delete(3)
        self.assertFalse(self.leftheavy.contains(3))
        self.assertEqual(self.leftheavy.size(), 3)

    def test_remove_one_child_right(self):
        """Test delete node one child, right."""
        self.rightheavy.delete(6)
        self.assertFalse(self.rightheavy.contains(6))
        self.assertEqual(self.rightheavy.size(), 5)

    def test_remove_one_child_right_on_left(self):
        """Test delete node that is left child with one child, right."""
        self.one.insert(2)
        self.one.insert(4)
        self.one.delete(2)
        self.assertFalse(self.one.contains(2))
        self.assertEqual(self.one.size(), 2)

    def test_remove_one_child_left_on_right(self):
        """Test delete node that is right child with one child, left."""
        self.one.insert(7)
        self.one.insert(6)
        self.one.delete(7)
        self.assertFalse(self.one.contains(7))
        self.assertEqual(self.one.size(), 2)

    def test_remove_one_child_root(self):
        """Test delete node that is root with one child."""
        self.one.insert(7)
        self.one.delete(5)
        self.assertFalse(self.one.contains(5))
        self.assertEqual(self.one.size(), 1)
        self.assertEqual(self.one.root.val, 7)

    def test_delete_two_children(self):
        """Test delete node with two children."""
        self.balance.delete(3)
        self.assertFalse(self.balance.contains(3))
        self.assertEqual(self.balance.size(), 6)

    def test_delete_two_children_root(self):
        """Test delete node with two children root."""
        self.balance.delete(5)
        self.assertFalse(self.balance.contains(5))
        self.assertEqual(self.balance.size(), 6)
        self.assertEqual(self.balance.root.val, 7)

if __name__ == '__main__':
    unittest.main()      
