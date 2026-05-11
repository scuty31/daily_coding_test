# 상자넣기
# https://www.acmicpc.net/problem/1965


def solution():
    n = int(input())
    boxes = list(map(int, input().split()))
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if boxes[i] > boxes[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


print(solution())