from typing import List


def factorizer(number: int) -> List[int]:
    i = 2
    mults = []
    while i * i <= number:
        while number % i == 0:
            mults.append(i)
            number = int(number / i)
        i = i + 1
    if number > 1:
        mults.append(number)
    return mults


result = factorizer(int(input()))
print(" ".join(map(str, result)))
