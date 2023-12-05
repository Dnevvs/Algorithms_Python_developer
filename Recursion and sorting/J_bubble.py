# ID решения ______
from typing import List


def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        check = 0
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                check = 1
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if check == 0:
            break
        print(' '.join(map(str, arr)))
    if i == 0:
        print(' '.join(map(str, arr)))


def read_input() -> List[int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    return arr


def main():
    arr = read_input()
    bubble(arr)


if __name__ == '__main__':
    main()
