# 돌 게임
# https://www.acmicpc.net/problem/9655


def solution():
    n = int(input())
    winner = ''

    if n % 2 == 0:
        winner = 'CY'
    else:
        winner = "SK"

    return winner


print(solution())