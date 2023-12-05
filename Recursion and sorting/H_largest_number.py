# ID решения ______
from typing import List


def compare_objects(object1, object2):
    if len(object1) == len(object2):
        return object1 > object2
    else:
        return object1 + object2 > object2 + object1


def largest_number(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i
        while j > 0 and compare_objects(temp, arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    print(''.join(map(str, arr)))


def read_input() -> List[int]:
    n = int(input())
    arr = list(input().strip().split())
    return arr


def main():
    arr = read_input()
    largest_number(arr)


if __name__ == '__main__':
    main()
