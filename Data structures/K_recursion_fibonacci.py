def recursion_fibonacci(intern: int, x) -> int:
    if intern == 0 or intern == 1:
        return 1
    return recursion_fibonacci(intern - 1, x) + recursion_fibonacci(intern - 2, x)


def read_input() -> int:
    intern = int(input())
    return intern


def main():
    intern = read_input()
    print(recursion_fibonacci(intern, 0))


if __name__ == '__main__':
    main()
