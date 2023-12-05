from typing import Tuple


def module_fibonacci(intern, k):
    if intern == 0:
        return 0, 1
    else:
        a, b = module_fibonacci(intern // 2, k)
        c = a * (2 * b - a) % k
        d = (a ** 2 + b ** 2) % k
        if intern % 2 == 0:
            return c, d
        else:
            return d, (c + d) % k


def read_input() -> Tuple[int, int]:
    args = list(input().strip().split())
    return int(args[0]), int(args[1])


def main():
    intern, k = read_input()
    print(module_fibonacci(intern + 1, 10 ** k)[0])


if __name__ == '__main__':
    main()
