from typing import List, Tuple


def diff_index(islands: List[int], k: int) -> int:
    min_diff = 0
    max_diff = islands[-1] - islands[0]
    while min_diff < max_diff:
        mid_diff = (min_diff + max_diff) // 2
        n = 0
        j = 0
        for i in range(len(islands)):
            while islands[i] - islands[j] > mid_diff:
                j += 1
            n += i - j
        if n >= k:
            max_diff = mid_diff
        else:
            min_diff = mid_diff + 1
    return min_diff


def read_input() -> Tuple[List[int], List[int]]:
    _ = int(input())
    islands = sorted(list(map(int, input().split())))
    k = int(input())
    return islands, k


def main() -> None:
    islands, k = read_input()
    print(diff_index(islands, k))


if __name__ == '__main__':
    main()
