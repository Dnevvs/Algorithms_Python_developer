# ID решения ______

buttons_list = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


def combinations(buttons, i, sequence, result):
    if i == len(buttons):
        result.append(sequence)
        return
    if buttons[i] not in buttons_list:
        return
    for letter in buttons_list[buttons[i]]:
        combinations(buttons, i + 1, sequence + letter, result)


def read_input() -> int:
    buttons = list(input().strip())
    return buttons


def main():
    buttons = read_input()
    result = []
    combinations(buttons, 0, '', result)
    for combination in result:
        print(combination, end=' ')


if __name__ == '__main__':
    main()
