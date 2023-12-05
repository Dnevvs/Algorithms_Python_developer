class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root, is_bs=True):
    if root is None:
        return True, None
    curr_val = root.value
    is_bs_left, left_val = solution(root.left, is_bs)
    is_bs_right, right_val = solution(root.right, is_bs)
    if (is_bs_left and is_bs_right and left_val and right_val and
       left_val < curr_val and right_val > curr_val):
        return True, curr_val
    return False, curr_val


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == "__main__":
    test()
