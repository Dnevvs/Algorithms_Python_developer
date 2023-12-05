from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    # first_number = '1100'
    # second_number = '101111'
    n1 = len(first_number)
    n2 = len(second_number)
    bs = ''
    if n1 > n2:
        n = n1
        fn = first_number
        m = n2
        sn = second_number
    else:
        n = n2
        fn = second_number
        m = n1
        sn = first_number
    ost = 0
    for i in range(n):
        if i > m - 1:
            r = int(fn[n - 1 - i]) + ost
            if r > 1:
                ost = 1
                r = r - int(r / 2) * 2
            else:
                ost = 0
        else:
            r = int(fn[n - 1 - i]) + int(sn[m - 1 - i]) + ost
            if r > 1:
                ost = 1
                r = r - int(r / 2) * 2
            else:
                ost = 0
        bs += str(r)
    if ost == 1:
        bs += '1'
    if bs == '':
        bs = '0'
    else:
        bs = bs[::-1]
    return bs


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
