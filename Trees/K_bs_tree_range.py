class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_range(node, left, right):
    if node.left is not None and node.value >= left:
        print_range(node.left, left, right)
    if left <= node.value <= right:
        print(node.value)
    if node.right is not None and node.value <= right:
        print_range(node.right, left, right)


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, node1)
    node3 = Node(8, None, None)
    node4 = Node(8, None, node3)
    node5 = Node(9, node4, None)
    node6 = Node(10, node5, None)
    node7 = Node(5, node2, node6)
    print_range(node7, 2, 8)


if __name__ == "__main__":
    test()
