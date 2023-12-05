
def merge_sort(arr: list, left: int, right: int) -> None:
    if right - left <= 1:
        return
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)
    merge(arr, left, mid, right)


def merge(arr: list, left: int, mid: int, right: int):
    left_arr = arr[left: mid]
    right_arr = arr[mid: right]
    i, r = 0, 0
    k = left
    while i < len(left_arr) and r < len(right_arr):
        if left_arr[i] <= right_arr[r]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[r]
            r += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while r < len(right_arr):
        arr[k] = right_arr[r]
        r += 1
        k += 1
    return arr


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    # print(b)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    # print(c)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


# def main():
#    test()


# if __name__ == '__main__':
#    main()
