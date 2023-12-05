from typing import Tuple, List


def transposition(servers_number: int, requests_number: int,
                  matrix) -> List[List]:
    matrix_new = []
    for i in range(servers_number):
        matrix_new.append([0] * requests_number)
    for i in range(servers_number):
        for j in range(requests_number):
            matrix_new[i][j] = matrix[j][i]
    return matrix_new


def read_input() -> Tuple[int, int, List[List]]:
    requests_number = int(input())
    servers_number = int(input())
    matrix = []
    for i in range(requests_number):
        matrix.append(list(map(int, input().strip().split())))
    return servers_number, requests_number, matrix


def main():
    servers_number, requests_number, matrix = read_input()
    matrix = transposition(servers_number, requests_number, matrix)
    for i in range(servers_number):
        result = ' '.join(map(str, matrix[i]))
        print(result)


if __name__ == '__main__':
    main()
