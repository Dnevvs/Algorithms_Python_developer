def get_longest_word(line: str) -> str:
    result = ''
    words = list(line.split())
    for word in words:
        if len(word) > len(result):
            result = word
    return result


def read_input() -> str:
    _ = input()
    line = input().strip()
    # line = 'i love segment tree'
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
