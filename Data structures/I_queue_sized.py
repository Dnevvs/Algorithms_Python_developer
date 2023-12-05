from typing import List, Tuple


class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')
            return None

    def pop(self):
        if self.is_empty():
            print('None')
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        print(x)
        return x

    def peek(self):
        if len(self.queue) == 0:
            print('None')
            return None
        else:
            print(self.queue[self.head])
            return self.queue[self.head]


def read_input() -> Tuple[int, List]:
    commands_number = int(input())
    queue_size = int(input())
    commands_list = []
    for i in range(commands_number):
        commands_list.append(list(input().strip().split()))
    return queue_size, commands_list


def main():
    queue_size, commands_list = read_input()
    queue = MyQueueSized(queue_size)
    for i in range(len(commands_list)):
        command_type = commands_list[i][0]
        if command_type == 'pop':
            queue.pop()
        if command_type == 'push':
            queue.push(int(commands_list[i][1]))
        if command_type == 'peek':
            queue.peek()
        if command_type == 'size':
            print(queue.size)


if __name__ == '__main__':
    main()
