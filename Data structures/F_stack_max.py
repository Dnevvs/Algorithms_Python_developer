from typing import List


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item: int):
        self.items.append(item)

    def pop(self):
        if not self.items:
            print('error')
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        if not self.items:
            print('None')
            return None
        x = max(self.items)
        print(x)
        return x


def read_input() -> List:
    commands_number = int(input())
    commands_list = []
    for i in range(commands_number):
        commands_list.append(list(input().strip().split()))
    return commands_list


def main():
    stack = StackMax()
    commands_list = read_input()
    for i in range(len(commands_list)):
        arg = ''
        if len(commands_list[i]) > 1:
            arg = commands_list[i][1]
        command = 'stack.'+commands_list[i][0]+'('+arg+')'
        eval(command)


if __name__ == '__main__':
    main()
