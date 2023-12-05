# ID 85978282
def golden_middle():
    left_len = int(input())
    right_len = int(input())
    left = list(map(int, input().split()))
    right = list(map(int, input().split()))
    res_len = left_len + right_len

    result = [0] * res_len
    i, r, k = 0, 0, 0
    while i < left_len and r < right_len:
        if left[i] <= right[r]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # while i < left_len:
    #    result[k] = left[i]
    #    i += 1
    #    k += 1
    # while r < right_len:
    #    result[k] = right[r]
    #    r += 1
    #    k += 1

    if i < left_len:
        result[k:] = left[i:]
    if r < right_len:
        result[k:] = right[r:]

    x = len(result) // 2
    if len(result) % 2:
        print(result[x])
        return
    print((result[x] + result[x - 1]) / 2)


def main() -> None:
    golden_middle()


if __name__ == '__main__':
    main()
