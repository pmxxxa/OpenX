class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if type(data) == int:
            self._data = data
        else:
            raise TypeError("Data should be an integer!")


def sum_nodes(node):
    if node is None:
        return 0
    return node.data + sum_nodes(node.left) + sum_nodes(node.right)


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def average(root):
    if root is None:
        return 0
    return sum_nodes(root) / count_nodes(root)


if __name__ == '__main__':
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

    print(sum_nodes(root))
    print(average(root))