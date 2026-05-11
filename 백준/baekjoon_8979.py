# 올림픽
# https://www.acmicpc.net/problem/8979


def solution():
    n, k = map(int, input().split())
    nation = []

    for _ in range(n):
        medal = list(map(int, input().split()))
        if medal[0] == k:
            nation.insert(0, medal)
        else:
            nation.append(medal)

    nation.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

    rate = 1

    for i in range(n):
        if nation[i][0] == k:
            rate += i
            break

    return rate


print(solution())