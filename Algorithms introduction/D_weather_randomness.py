from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    n = len(temperatures)
    if n == 1:
        return 1
    chaos = 0
    for i in range(n):
        if i == 0:
            if temperatures[i] > temperatures[i+1]:
                chaos += 1
        elif i == n-1:
            if temperatures[i] > temperatures[i-1]:
                chaos += 1
        else:
            if (temperatures[i] > temperatures[i-1] and
               temperatures[i] > temperatures[i+1]):
                chaos += 1
    return chaos


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
