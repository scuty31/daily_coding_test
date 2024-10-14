from collections import deque



def solution():
	n, m = map(int, input().split())
	maps = list()
	visited = [[[1e9, 1e9, 1e9] for _ in range(m)] for _ in range(n)]
	answer = 1e9

	for _ in range(n):
		maps.append(list(map(int, input().split())))

	# 시작 부분 초기화
	for i in range(m):
		visited[0][i] = [maps[0][i], maps[0][i], maps[0][i]]

	for i in range(1, n):
		for j in range(m):
			for d in range(3):
				if (j == 0 and d == 2) or (j == m-1 and d == 0):
					continue

				for k in range(3):
					if d == k:
						continue

					visited[i][j][d] = min(visited[i][j][d], visited[i-1][j-d+1][k] + maps[i][j])

	for i in range(m):
		for j in range(3):
			answer = min(answer, visited[-1][i][j])

	return answer



print(solution())