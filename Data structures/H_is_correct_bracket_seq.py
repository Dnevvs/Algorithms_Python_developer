
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
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


def is_correct_bracket_seq(stack, sequence):
    # sequence = '(({})({[]}[])'
    if len(sequence) == 0:
        return True
    for i in range(len(sequence)):
        bracket = sequence[i]
        if stack.size() > 0:
            prev_bracket = stack.items[-1]
            if ((bracket == ')' and prev_bracket == '(') or
               (bracket == '}' and prev_bracket == '{') or
               (bracket == ']' and prev_bracket == '[')):
                stack.pop()
                continue
        stack.push(bracket)
    if stack.size() == 0:
        return True
    return False


def read_input() -> str:
    sequence = input().strip()
    return sequence


def main():
    stack = Stack()
    sequence = read_input()
    print(is_correct_bracket_seq(stack, sequence))


if __name__ == '__main__':
    main()
