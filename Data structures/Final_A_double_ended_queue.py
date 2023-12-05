# ID решения 84840403
from typing import List, Tuple


class DoubleEndedQueue:
    def __init__(self, max_len):
        self.__queue = [None] * max_len
        self.__max_len = max_len
        self.__head = 0
        self.__tail = 0
        self.size = 0

    def push_front(self, value):
        if self.size == self.__max_len:
            return 'error'
        self.__head = (self.__head - 1) % self.__max_len
        self.__queue[self.__head] = value
        self.size += 1

    def pop_front(self, *args):
        if self.size == 0:
            return 'error'
        value = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_len
        self.size -= 1
        return value

    def push_back(self, value):
        if self.size == self.__max_len:
            return 'error'
        self.__queue[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_len
        self.size += 1

    def pop_back(self, *args):
        if self.size == 0:
            return 'error'
        self.__tail = (self.__tail - 1) % self.__max_len
        value = self.__queue[self.__tail]
        self.__queue[self.__tail] = None
        self.size -= 1
        return value


def read_input() -> Tuple[int, List]:
    commands_number = int(input())
    max_len = int(input())
    commands_list = []
    for i in range(commands_number):
        commands_list.append(list(input().strip().split()))
        if len(commands_list[i]) == 1:
            commands_list[i].append(None)
        else:
            commands_list[i][1] = int(commands_list[i][1])

    return max_len, commands_list


def main():
    max_len, commands_list = read_input()
    queue = DoubleEndedQueue(max_len)
    commands_dict = {
        'push_front': queue.push_front,
        'pop_front': queue.pop_front,
        'push_back': queue.push_back,
        'pop_back': queue.pop_back,
    }
    for i in range(len(commands_list)):
        result = commands_dict[commands_list[i][0]](commands_list[i][1])
        if result is not None:
            print(result)


if __name__ == '__main__':
    main()
