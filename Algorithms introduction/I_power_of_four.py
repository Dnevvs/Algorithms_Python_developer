def is_power_of_four(number: int) -> bool:
    if number == 1:
        return True
    ost = number
    while ost > 0:
        ost = int(number / 4)
        diff = number - ost * 4
        if ost == 1 and diff <= 0:
            return True
        if diff > 0:
            return False
        number = ost
    return True


print(is_power_of_four(int(input())))
