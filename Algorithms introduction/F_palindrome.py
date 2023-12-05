import re


def is_palindrome(line: str) -> bool:
    # line = 'A man, a plan, a canal: Panama'
    # line = 'zo'
    # print(line)
    line = line.lower()
    # print(line)
    line = re.sub("[^a-z0-9]", "", line)
    # print(line)
    n = len(line)
    for i in range(n):
        if line[i] != line[n-1-i]:
            return False
    return True


print(is_palindrome(input().strip()))
