from typing import List, Tuple


def part_sort(n_len: int, nums: List[int]) -> int:
    n = 0
    v = 0
    j = 0
    i = 0
    while i < n_len:
        v += nums[i]
        j += i
        if v == j:
            n += 1
            v = 0
            j = 0
        i += 1
    return n


def read_input() -> Tuple[int, List[int]]:
    n_len = int(input())
    nums = list(map(int, input().split()))
    return n_len, nums


def main() -> None:
    n_len, nums = read_input()
    print(part_sort(n_len, nums))


if __name__ == '__main__':
    main()
