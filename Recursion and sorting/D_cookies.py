from typing import List, Tuple


def happy_babies(children_greed: List, cookies_sizes: List) -> int:
    happy_baby = 0
    for i in range(len(children_greed)):
        if cookies_sizes and children_greed[i] <= cookies_sizes[-1]:
            cookies_sizes.pop()
            happy_baby += 1
    return happy_baby


def read_input() -> Tuple[List[List], List[List]]:
    _ = int(input())
    children_greed = sorted(list(map(int, input().split())), reverse=True)
    _ = int(input())
    cookies_sizes = sorted(list(map(int, input().split())))
    return children_greed, cookies_sizes


def main() -> None:
    children_greed, cookies_sizes = read_input()
    happy_baby = happy_babies(children_greed, cookies_sizes)
    print(happy_baby)


if __name__ == '__main__':
    main()
