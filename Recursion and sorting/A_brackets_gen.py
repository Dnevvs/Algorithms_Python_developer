# ID решения ______


class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def pop(self):
        if not self.items:
            print('error')
            return None
        self.size -= 1
        return self.items.pop()


def is_correct_bracket_seq(sequence):
    if len(sequence) == 0:
        return True
    stack = Stack()
    for i in range(len(sequence)):
        bracket = sequence[i]
        if stack.size > 0:
            prev_bracket = stack.items[-1]
            if bracket == ')' and prev_bracket == '(':
                stack.pop()
                continue
        stack.push(bracket)
    if stack.size == 0:
        return True
    return False


def brackets_gen(sequence_len, sequence):
    if sequence_len == 0:
        if is_correct_bracket_seq(sequence):
            print(sequence)
    else:
        brackets_gen(sequence_len - 1, sequence + '(')
        brackets_gen(sequence_len - 1, sequence + ')')


def read_input() -> int:
    sequence_len = int(input())
    return sequence_len


def main():
    sequence_len = read_input()
    sequence = ''
    brackets_gen(sequence_len * 2, sequence)


if __name__ == '__main__':
    main()
