# ID решения ______


def issubsequence(string1, string2):
    isfind = -1
    for i in string1:
        isfind = string2.find(i, isfind + 1)
        if isfind == - 1:
            return False
    return True


def read_input():
    string1 = input().strip()
    string2 = input().strip()
    return string1, string2


def main():
    string1, string2 = read_input()
    print(issubsequence(string1, string2))


if __name__ == '__main__':
    main()
