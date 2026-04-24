import sys
from collections import deque

input = sys.stdin.readline


def check_num(r, c):
    if r == 0 and c == 0:
        return 0
    elif r == 0 and c == 1:
        return 1
    elif r == 1 and c == 0:
        return 2
    elif r == 1 and c == 1:
        return 3


def half_side(n, r, c):
    next_n = n-1
    half_n = 2**next_n
    area_n = half_n * half_n
    result = 0

    # 1사분면
    if r < half_n and c < half_n:
        if n > 1:
            result += half_side(next_n, r, c)

    # 2사분면
    elif r < half_n <= c:
        if n > 1:
            result += area_n
            result += half_side(next_n, r, c-half_n)

    # 3사분면
    elif r >= half_n > c:
        if n > 1:
            result += area_n * 2
            result += half_side(next_n, r-half_n, c)

    # 4사분면
    else:
        if n > 1:
            result += area_n * 3
            result += half_side(next_n, r-half_n, c-half_n)

    if n == 1:
        result += check_num(r, c)

    return result



def solution():
    n, r, c = map(int, input().split())

    answer = half_side(n, r, c)

    return answer


print(solution())