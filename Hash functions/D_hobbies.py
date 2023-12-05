from typing import List


def read_input() -> List:
    _ = int(input())
    hobbies = []
    for i in range(_):
        hobbies.append(input().strip())
    return hobbies


def main() -> None:
    hobbies = read_input()
    result = sorted(set(hobbies), key=lambda x: hobbies.index(x))
    for i in range(len(result)):
        print(result[i])


if __name__ == '__main__':
    main()
