class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    if root is None:
        return -1
    bright = root.value
    l_bright = solution(root.left)
    r_bright = solution(root.right)
    if l_bright > bright:
        bright = l_bright
    if r_bright > bright:
        bright = r_bright
    return bright


def test():
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(4, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 4


if __name__ == "__main__":
    test()
