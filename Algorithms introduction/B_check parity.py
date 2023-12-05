def check_parity(a: int, b: int, c: int) -> bool:
    result = ((a % 2 == 0 and b % 2 == 0 and c % 2 == 0) or
              (a % 2 != 0 and b % 2 != 0 and c % 2 != 0))
    return result


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
