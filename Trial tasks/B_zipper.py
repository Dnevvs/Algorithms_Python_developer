from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    # Здесь реализация вашего решения
    n = len(a)
    c = []
    for i in range(0, n):
        c.append(a[i])
        c.append(b[i])
    return c


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
