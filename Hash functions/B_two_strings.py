import random
import string


def hash_string(bm: int, module: int, str_in: str) -> int:
    hash = 0
    sum_hash = 1
    str_in = str_in[::-1]
    for sym in str_in:
        hash = ((hash + ord(sym) * sum_hash) % module)
        sum_hash = (sum_hash * bm) % module
    return hash


def main() -> None:
    bm = 1000
    module = 123987123
    alphabet = string.ascii_lowercase
    hash_dict = {}
    i = 1
    while True:
        str_in = ''.join(random.choice(alphabet) for i in range(10))
        hash = hash_string(bm, module, str_in)
        if not hash_dict.get(hash):
            hash_dict[hash] = str_in
            i += 1
        else:
            print(hash_dict[hash])
            print(str_in)
            print(hash)
            print(i)
            break


if __name__ == '__main__':
    main()
