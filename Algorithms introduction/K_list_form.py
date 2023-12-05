from typing import List, Tuple


def get_sum(x_list: List[int], k: int) -> List[int]:
    k_list = [int(i) for i in str(k)]
    k_list.reverse()
    x_list.reverse()
    n = max(len(x_list), len(k_list))
    k_list = k_list + [0] * (n - len(k_list))
    x_list = x_list + [0] * (n - len(x_list))
    n_list = []
    ost = 0
    for i in range(n):
        r = x_list[i] + k_list[i] + ost
        if r > 9:
            ost = 1
            r = r - 10
        else:
            ost = 0
        n_list.append(r)
    if ost == 1:
        n_list.append(ost)
    n_list.reverse()
    return n_list


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))

