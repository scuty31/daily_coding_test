# https://www.acmicpc.net/problem/2531
# 회전 초밥


def solution():
	n, d, k, c = map(int, input().split())
	sushi = list()
	sushi_num = {i: 0 for i in range(1, d+1)}

	for _ in range(n):
		sushi.append(int(input()))

	# 마지막 번 초밥부터 먹는 경우의 수를 구하기 위해 앞 부분의 초밥 추가
	sushi += sushi[:(k-1)]
	cnt = 0

	j = 0
	for j in range(k):
		sushi_num[sushi[j]] += 1

	cnt =

	for i in range(1, n):





solution()