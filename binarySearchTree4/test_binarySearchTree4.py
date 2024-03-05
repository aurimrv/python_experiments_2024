import unittest
from binarySearchTree4 import Bst
from results import Results
from dfs import in_order_traversal

class TestTree(unittest.TestCase):

    def test_tree_one(self):
        results = Results()
        bst = Bst()
        bst.insert(5)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        in_order_traversal(bst.root, results.add_result)
        self.assertEqual(str(results), '[1, 2, 3, 5, 8]')
        results.clear_results()

    def test_tree_two(self):
        results = Results()
        bst = Bst()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        in_order_traversal(bst.root, results.add_result)
        self.assertEqual(str(results), '[1, 2, 3, 4, 5]')

        print('Success: test_tree')

if __name__ == '__main__':
    unittest.main()