from typing import List


class StackMaxEffective:
    def __init__(self):
        self.items = []

    def push(self, item: int):
        if self.items:
            max_item = max(item, self.items[-1][1])
        else:
            max_item = item
        self.items.append((item, max_item))

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
        x = self.items[-1][1]
        print(x)
        return x


def read_input() -> List:
    commands_number = int(input())
    commands_list = []
    for i in range(commands_number):
        commands_list.append(list(input().strip().split()))
    return commands_list


def main():
    stack = StackMaxEffective()
    commands_list = read_input()
    for i in range(len(commands_list)):
        command_type = commands_list[i][0]
        if command_type == 'pop':
            stack.pop()
        if command_type == 'push':
            stack.push(int(commands_list[i][1]))
        if command_type == 'get_max':
            stack.get_max()


if __name__ == '__main__':
    main()
