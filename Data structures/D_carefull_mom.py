# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False
# LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def get_index_by_value(node, value):
    index = -1
    while True:
        index += 1
        if node.value == value:
            break
        node = node.next_item
        if node is None:
            index = -1
            break
    return index


def solution(node, value):
    index = get_index_by_value(node, value)
    return index


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2


if __name__ == '__main__':
    test()