# ID решения 84841354
from typing import List


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def reversed_calc(stack, sequence):
    s_len = len(sequence)
    if s_len == 0:
        return None
    commands_dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }
    for i in range(s_len):
        item = sequence[i]
        if stack.size() > 1 and item in commands_dict.keys():
            operand2 = int(stack.pop())
            operand1 = int(stack.pop())
            result = commands_dict[item](operand1, operand2)
            stack.push(result)
            continue
        stack.push(item)
    if stack.size() == 0:
        return None
    return stack.items[-1]


def read_input() -> List:
    sequence = list(input().strip().split())
    return sequence


def main():
    stack = Stack()
    sequence = read_input()
    print(reversed_calc(stack, sequence))


if __name__ == '__main__':
    main()
