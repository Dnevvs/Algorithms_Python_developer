def max_subs(str_in):
    subs = ''
    in_len = len(str_in)
    s_len = 0
    max_len = 0
    for i in range(in_len):
        if str_in[i] not in subs:
            subs += str_in[i]
            s_len += 1
        else:
            index = subs.index(str_in[i])
            subs = subs[index + 1:] + str_in[i]
            s_len = len(subs)
        if s_len > max_len:
            max_len = s_len
    return max_len


def read_input() -> str:
    return input().strip()


def main() -> None:
    str_in = read_input()
    result = max_subs(str_in)
    print(result)


if __name__ == '__main__':
    main()
