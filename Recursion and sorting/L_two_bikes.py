# ID решения ______
from typing import List, Tuple


def by_bike(bike_price, days_list, left, right):
    if right <= left and left != 0:
        return -1
    mid = (left + right) // 2
    if (days_list[mid] >= bike_price and
       (days_list[mid - 1] < bike_price or mid == 0)):
        return mid + 1
    elif days_list[mid] >= bike_price:
        return by_bike(bike_price, days_list, left, mid)
    else:
        return by_bike(bike_price, days_list, mid + 1, right)


def read_input() -> Tuple[int, List, int]:
    days_number = int(input())
    days_list = list(map(int, input().strip().split()))
    bike_price = int(input())
    return bike_price, days_list, days_number


def main():
    bike_price, days_list, days_number = read_input()
    day1 = by_bike(bike_price, days_list, left=0, right=days_number)
    day2 = by_bike(bike_price * 2, days_list, left=0, right=days_number)
    print(day1, day2)


if __name__ == '__main__':
    main()
