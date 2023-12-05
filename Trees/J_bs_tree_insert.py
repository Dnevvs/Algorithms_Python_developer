
class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def insert(root, key) -> Node:
    if key < root.value:
        if root.left is None:
            root.left = Node(key)
        else:
            insert(root.left, key)
    if key >= root.value:
        if root.right is None:
            root.right = Node(key)
        else:
            insert(root.right, key)
    return root


def test():
    node1 = Node(7, None, None)
    node2 = Node(8, node1, None)
    node3 = Node(7, None, node2)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()
