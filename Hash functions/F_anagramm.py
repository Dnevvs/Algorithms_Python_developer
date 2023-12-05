from typing import List


def read_input() -> List:
    _ = int(input())
    array = [tuple(sorted(list(x))) for x in input().strip().split()]
    return array


def main() -> None:
    array = read_input()
    result = {}
    for i in range(len(array)):
        result[array[i]] = result.get(array[i], '') + str(i) + ' '
    print(*result.values(), sep='\n')


if __name__ == '__main__':
    main()
