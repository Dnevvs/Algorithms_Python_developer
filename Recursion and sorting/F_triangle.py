from typing import List, Tuple


def triangle_length(sides_lengths: List[int]) -> int:
    n = len(sides_lengths)
    if n < 3:
        return -1
    triangle_len = 0
    c = 0
    a = 1
    b = 2
    while b < n:
        if sides_lengths[c] < sides_lengths[a] + sides_lengths[b]:
            triangle_len = (sides_lengths[a] + sides_lengths[b] +
                            sides_lengths[c])
            break
        c += 1
        a += 1
        b += 1
    return triangle_len


def read_input() -> Tuple[List]:
    _ = int(input())
    sides_lengths = sorted(list(map(int, input().split())), reverse=True)
    return sides_lengths


def main() -> None:
    sides_lengths = read_input()
    triangle_len = triangle_length(sides_lengths)
    print(triangle_len)


if __name__ == '__main__':
    main()
