from typing import List, Tuple


def highschools_rating(highschools: List[int]) -> List[int]:
    rating = [[i, 0] for i in range(highschools[-1] + 1)]
    for value in highschools:
        rating[value][1] += 1
    rating.sort(key=lambda x: x[1], reverse=True)
    return rating


def read_input() -> Tuple[List, int]:
    _ = int(input())
    highschools = sorted(list(map(int, input().split())))
    rating_len = int(input())
    return highschools, rating_len


def main() -> None:
    highschools, rating_len = read_input()
    rating = highschools_rating(highschools)
    for i in range(rating_len):
        print(rating[i][0], end=' ')


if __name__ == '__main__':
    main()
