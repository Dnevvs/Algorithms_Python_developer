# ID решения ______
from typing import List


def counting_sort(array, k):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1
    index = 0
    for value in range(k):
        for amount in range(1, counted_values[value]+1):
            array[index] = value
            index += 1
    return array


def read_input() -> List[int]:
    n = int(input())
    clothes = list(map(int, input().strip().split()))
    return clothes


def main():
    clothes = read_input()
    sorted_clothes = counting_sort(clothes, 3)
    print(' '.join(map(str, sorted_clothes)))


if __name__ == '__main__':
    main()
