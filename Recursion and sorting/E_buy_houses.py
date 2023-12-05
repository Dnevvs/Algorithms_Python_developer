from typing import List, Tuple


def buy_houses(budget: int, houses_prices: List) -> int:
    houses_number = 0
    amount = 0
    i = 0
    while i < len(houses_prices) and amount + houses_prices[i] <= budget:
        amount += houses_prices[i]
        houses_number += 1
        i += 1

    return houses_number


def read_input() -> Tuple[int, List[List]]:
    _, budget = map(int, input().split())
    houses_prices = sorted(list(map(int, input().split())))
    return budget, houses_prices


def main() -> None:
    budget, houses_prices = read_input()
    houses_number = buy_houses(budget, houses_prices)
    print(houses_number)


if __name__ == '__main__':
    main()
