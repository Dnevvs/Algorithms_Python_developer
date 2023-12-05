from typing import Tuple


def hash_string(bm: int, module: int, string: str) -> int:
    hash = 0
    sum_hash = 1
    string = string[::-1]
    for sym in string:
        hash = ((hash + ord(sym) * sum_hash) % module)
        sum_hash = (sum_hash * bm) % module
    return hash


def read_input() -> Tuple[int, int, str]:
    bm = int(input())
    module = int(input())
    string = input().strip()
    return bm, module, string


def main() -> None:
    bm, module, string = read_input()
    hash = hash_string(bm, module, string)
    print(hash)


if __name__ == '__main__':
    main()
