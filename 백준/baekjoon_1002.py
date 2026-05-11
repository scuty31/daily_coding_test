# 터렛
# https://www.acmicpc.net/problem/1002


import math


def solution():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    answer = 0

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            answer = -1
        else:
            answer = 0
    else:
        if r1 + r2 > dist > abs(r1 - r2):
            answer = 2
        elif r1 + r2 == dist or abs(r1 - r2) == dist:
            answer = 1
        else:
            answer = 0

    return answer


t = int(input())

for _ in range(t):
    print(solution())

