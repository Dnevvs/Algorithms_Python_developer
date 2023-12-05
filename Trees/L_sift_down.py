def pop_max(heap):
    result = heap[1]
    heap[1] = heap[-1]
    sift_down(heap, 1)
    return result


def sift_down(heap, index):
    left = 2 * index
    right = 2 * index + 1
    if len(heap)-1 < left:
        return index
    if (right <= len(heap)-1) and (heap[left] < heap[right]):
        index_largest = right
    else:
        index_largest = left
    if heap[index] < heap[index_largest]:
        tmp = heap[index]
        heap[index] = heap[index_largest]
        heap[index_largest] = tmp
        return sift_down(heap, index_largest)
    return index


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()
