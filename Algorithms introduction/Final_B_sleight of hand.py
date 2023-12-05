# ID решения 84285435
from typing import Tuple


def get_score(buttons_list: str, buttons_number: int) -> int:
    score = 0
    buttons = {}
    for i in range(1, 10):
        buttons[str(i)] = 0
    for i in range(len(buttons_list)):
        n = buttons_list[i]
        if n != '.':
            buttons[n] += 1
    for i in range(1, 10):
        n = str(i)
        if buttons[n] != 0 and buttons_number >= buttons[n]:
            score += 1
    return score


def read_input(players_number: int, keyboard_size: int) -> Tuple[str, int]:
    buttons_number = int(input()) * players_number
    buttons_list = ''
    for i in range(keyboard_size):
        buttons_list += input().strip()
    return buttons_list, buttons_number


def main():
    players_number = 2
    keyboard_size = 4
    buttons_list, buttons_number = read_input(players_number, keyboard_size)
    result = str(get_score(buttons_list, buttons_number))
    print(result)


if __name__ == '__main__':
    main()
