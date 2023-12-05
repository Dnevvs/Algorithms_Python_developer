def to_binary(number: int) -> str:
    bs = ''
    num = number
    while num >= 1:
        num = int(number / 2)
        diff = number - num * 2
        bs += str(diff)
        number = num
    if bs == '':
        bs = '0'
    else:
        bs = bs[::-1]
    return bs


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
