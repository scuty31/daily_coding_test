# https://www.acmicpc.net/problem/15989
# 1, 2, 3 더하기 4


def solution():
	n = int(input())

	dp = [1] * (n+1)

	dp[1] = 1

	for i in range(2, n+1):
		dp[i] = dp[i] + dp[i-2]

	for j in range(3, n+1):
		dp[j] = dp[j] + dp[j-3]

	return dp[n]


t = int(input())

for _ in range(t):
	print(solution())