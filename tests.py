import unittest

from tree import Tree, sum_nodes, count_nodes, average

root = Tree(5)
root.left = Tree(3)
root.right = Tree(7)
root.left.left = Tree(2)
root.left.right = Tree(5)
root.right.left = Tree(1)
root.right.right = Tree(0)
root.right.right.left = Tree(2)
root.right.right.right = Tree(8)
root.right.right.right.right = Tree(5)


class TestTree(unittest.TestCase):
    def test_should_return_nodes_sum(self):
        self.assertEqual(38, sum_nodes(root))
        self.assertEqual(10, sum_nodes(root.left))
        self.assertEqual(2, sum_nodes(root.left.left))
        self.assertEqual(5, sum_nodes(root.left.right))
        self.assertEqual(23, sum_nodes(root.right))
        self.assertEqual(1, sum_nodes(root.right.left))
        self.assertEqual(15, sum_nodes(root.right.right))
        self.assertEqual(2, sum_nodes(root.right.right.left))
        self.assertEqual(13, sum_nodes(root.right.right.right))
        self.assertEqual(5, sum_nodes(root.right.right.right.right))

    def test_should_count_nodes(self):
        self.assertEqual(10, count_nodes(root))
        self.assertEqual(3, count_nodes(root.left))
        self.assertEqual(1, count_nodes(root.left.left))
        self.assertEqual(1, count_nodes(root.left.right))
        self.assertEqual(6, count_nodes(root.right))
        self.assertEqual(1, count_nodes(root.right.left))
        self.assertEqual(4, count_nodes(root.right.right))
        self.assertEqual(1, count_nodes(root.right.right.left))
        self.assertEqual(2, count_nodes(root.right.right.right))
        self.assertEqual(1, count_nodes(root.right.right.right.right))

    def test_should_count_nodes_average(self):
        self.assertEqual(3.8, average(root))
        self.assertLessEqual(3.33, average(root.left))
        self.assertEqual(2, average(root.left.left))
        self.assertEqual(5, average(root.left.right))
        self.assertLessEqual(3.83, average(root.right))
        self.assertEqual(1, average(root.right.left))
        self.assertEqual(3.75, average(root.right.right))
        self.assertEqual(2, average(root.right.right.left))
        self.assertEqual(6.5, average(root.right.right.right))
        self.assertEqual(5, average(root.right.right.right.right))

    def test_should_check_data_type(self):
        self.assertTrue(type(root.data) == int)
        self.assertTrue(type(root.left.data) == int)
        self.assertTrue(type(root.left.left.data) == int)
        self.assertTrue(type(root.left.right.data) == int)
        self.assertTrue(type(root.right.data) == int)
        self.assertTrue(type(root.right.left.data) == int)
        self.assertTrue(type(root.right.right.data) == int)
        self.assertTrue(type(root.right.right.left.data) == int)
        self.assertTrue(type(root.right.right.right.data) == int)
        self.assertTrue(type(root.right.right.right.right.data) == int)


if __name__ == '__main__':
    unittest.main()
