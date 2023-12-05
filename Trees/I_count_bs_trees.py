def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n


def count_bs_trees(n):
    result = int(fact(2 * n) / (fact(n) * fact(n + 1)))
    return result


def read_input():
    n = int(input())
    return n


def main():
    n = read_input()
    print(count_bs_trees(n))


if __name__ == "__main__":
    main()
