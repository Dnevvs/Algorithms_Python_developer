from typing import Tuple


def get_excessive_letter(s: str, t: str) -> str:
    for i in s:
        t = t.replace(i, '', 1)
    return t


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
