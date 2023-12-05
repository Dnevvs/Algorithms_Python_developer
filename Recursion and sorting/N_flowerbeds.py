# ID решения ______
from typing import List


# эта функция только для примера
def merge_sort(array):
    n = len(array)
    if n == 1:
        return array
    left = merge_sort(array[0: int(n/2)])
    right = merge_sort(array[int(n/2): n])
    result = [[]] * n
    i, r, k = 0, 0, 0
    while i < len(left) and r < len(right):
        if left[i] <= right[r]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1
    while i < len(left):
        result[k] = left[i]
        i += 1
        k += 1
    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1
    return result


def flowerbeds(segments):
    n = len(segments)
    flowerbeds = []
    start = segments[0][0]
    finish = segments[0][1]
    i = 0
    while i < n:
        if segments[i][0] <= finish:
            finish = max(finish, segments[i][1])
        else:
            flowerbeds.append([start, finish])
            start = segments[i][0]
            finish = segments[i][1]
        i += 1
    flowerbeds.append([start, finish])
    return flowerbeds


def read_input() -> List[List[int]]:
    n = int(input())
    segments = []
    for i in range(n):
        segments.append(list(map(int, input().strip().split())))
    return segments


def main():
    segments = read_input()
    segments.sort()
    flowerbeds_list = flowerbeds(segments)
    for i in range(len(flowerbeds_list)):
        print(' '.join(map(str, flowerbeds_list[i])))


if __name__ == '__main__':
    main()
