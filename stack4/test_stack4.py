import unittest
from stack4 import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.empty = Stack()
        self.one = Stack(5)
        self.multi = Stack([1, 2, 'three', 4, 5])

    def test_stack_is_initialized(self):
        self.assertEqual(self.empty._stack._length, 0)

    def test_empty_stack_push(self):
        self.empty.push(3)
        self.assertEqual(self.empty._stack._length, 1)

    def test_stack_of_one_push(self):
        self.one.push(2)
        self.assertEqual(self.one._stack.head.data, 2)

    def test_stack_of_multiple_push(self):
        self.multi.push(2)
        self.assertEqual(self.multi._stack.head.data, 2)

    def test_empty_stack_pop(self):
        with self.assertRaises(IndexError):
            self.empty.pop()

    def test_stack_of_one_pop(self):
        self.one.pop()
        self.assertIsNone(self.one._stack.head)

    def test_stack_of_multiple_pop(self):
        self.multi.pop()
        self.assertEqual(self.multi._stack.head.data, 4)

if __name__ == '__main__':
    unittest.main()
