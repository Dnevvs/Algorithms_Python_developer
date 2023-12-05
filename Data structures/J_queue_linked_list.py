from typing import List


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def put(self, item):
        new_node = Node(item)
        if self.size == 0:
            self.head = new_node
            self.size = 1
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
            self.size += 1
        return new_node

    def get(self):
        if self.size == 0:
            return ('error')
        x = self.head.value
        if self.size > 1:
            self.head = self.head.next
            self.size -= 1
        else:
            self.head = None
            self.size = 0
        return x


def read_input() -> List:
    commands_number = int(input())
    commands_list = []
    for i in range(commands_number):
        commands_list.append(list(input().strip().split()))
    return commands_list


def main():
    commands_list = read_input()
    queue = QueueLinkedList()
    for i in range(len(commands_list)):
        command_type = commands_list[i][0]
        if command_type == 'get':
            print(queue.get())
        if command_type == 'put':
            queue.put(int(commands_list[i][1]))
        if command_type == 'size':
            print(queue.size)


if __name__ == '__main__':
    main()
