# ID решения 85716997
import random
from typing import List, Tuple


def partition(array: List[List], pivot: List,
              left: int, right: int) -> Tuple[int, int]:
    while left <= right:
        while array[left] < pivot:
            left += 1
        while pivot < array[right]:
            right -= 1
        if left <= right:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            left += 1
            right -= 1
    return left, right


def quicksort(array: List[List], left: int = 0, right: int = None):
    if len(array) < 2:
        return
    if right is None:
        right = len(array) - 1
    if left >= right:
        return
    pivot = array[random.randint(left, right)]
    new_left, new_right = partition(array, pivot, left, right)
    quicksort(array, new_left, right)
    quicksort(array, left, new_right)


def read_input() -> Tuple[int, List[List]]:
    participants_number = int(input())
    participants = []
    for i in range(participants_number):
        participant = input().strip().split()
        participants.append([-int(participant[1]),
                             int(participant[2]),
                             participant[0]])
    return participants_number, participants


def main() -> None:
    participants_number, participants = read_input()
    quicksort(participants)
    for i in range(participants_number):
        print(participants[i][2])


if __name__ == '__main__':
    main()
