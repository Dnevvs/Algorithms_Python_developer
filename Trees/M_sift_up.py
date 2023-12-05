def heap_add(heap, key):
    index = len(heap)
    heap[index] = key
    sift_up(heap, index)


def sift_up(heap, index):
    if index == 1:
        return index
    parent_index = index // 2
    if heap[parent_index] < heap[index]:
        tmp = heap[parent_index]
        heap[parent_index] = heap[index]
        heap[index] = tmp
        return sift_up(heap, parent_index) 
    return index


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == '__main__':
    test()
