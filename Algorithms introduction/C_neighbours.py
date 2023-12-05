from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    nb = []
    if col >= 0 and row >= 0:
        n = len(matrix)
        if n > 0:
            m = len(matrix[0])
            if m > 0:
                if row > 0:
                    nb.append(matrix[row-1][col])
                if col < m - 1:
                    nb.append(matrix[row][col+1])
                if row < n - 1:
                    nb.append(matrix[row+1][col])
                if col > 0:
                    nb.append(matrix[row][col-1])
                nb.sort()
    return nb


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
