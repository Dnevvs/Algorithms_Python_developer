from typing import List, Tuple


def hash_subs(left, right, hashs, bm, module):
    if left == 0:
        return hashs[right]
    return (hashs[right] - hashs[left] * bm) % module


def hashs_string(bm: int, module: int, str_in: str) -> int:
    hashs = [0]
    sum_hashs = [1]
    # str_in = str_in[::-1]
    for i in range(len(str_in)):
        hashs.append((hashs[i] * bm + ord(str_in[i])) % module)
        sum_hashs.append((sum_hashs[i] * bm) % module)
    return hashs, sum_hashs


def read_input() -> Tuple[int, int, str, int, List[List]]:
    bm = int(input())
    module = int(input())
    str_in = input().strip()
    m_len = int(input())
    margins = []
    for i in range(m_len):
        margins.append(list(map(int, input().strip().split())))
    return bm, module, str_in, m_len, margins


def main() -> None:
    bm, module, str_in, m_len, margins = read_input()
    hashs, bms = hashs_string(bm, module, str_in)
    for i in range(m_len):
        res = hash_subs(margins[i][0]-1, margins[i][1],
                        hashs, bms[margins[i][1]-margins[i][0]+1], module)
        print(res)


if __name__ == '__main__':
    main()
