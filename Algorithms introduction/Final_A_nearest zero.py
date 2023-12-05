# ID решения 84285480	
from typing import List


def get_distance(lots_list: List[int]) -> List[int]:
    n = len(lots_list)
    lots_distance = [0] * n
    empty_lot = -n
    for i in range(n):
        if lots_list[i] > 0:
            lots_distance[i] = i - empty_lot
        else:
            empty_lot = i
    empty_lot = 2 * n
    for i in reversed(range(n)):
        if lots_list[i] > 0:
            lots_distance[i] = min(empty_lot - i, lots_distance[i])
        else:
            empty_lot = i
    return lots_distance


def read_input() -> List[int]:
    n = int(input())
    lots_list = list(map(int, input().strip().split()))
    return lots_list


def main():
    lots_list = read_input()
    result = ' '.join(map(str, get_distance(lots_list)))
    print(result)


if __name__ == '__main__':
    main()
