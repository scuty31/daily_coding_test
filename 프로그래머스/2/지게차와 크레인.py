from collections import deque


def check_side(storage, request):
	dx = [-1, 0, 1, 0]
	dy = [0, 1, 0, -1]
	q = deque()
	visited = [[False] * len(storage[0]) for _ in range(len(storage))]

	q.append((0, 0))
	visited[0][0] = True

	while q:
		x, y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if nx < 0 or ny < 0 or nx >= len(storage) or ny >= len(storage[0]):
				continue

			if visited[nx][ny]:
				continue

			if storage[nx][ny] == '.':
				q.append((nx, ny))
				visited[nx][ny] = True

			elif storage[nx][ny] == request:
				storage[nx][ny] = '.'
				visited[nx][ny] = True


def solution(storage, requests):
	answer = 0
	storage_list = [['.' for _ in range(len(storage[0]) + 2)]]
	for i in range(len(storage)):
		storage_list.append(list('.') + list(storage[i]) + list('.'))
	storage_list.append(['.' for _ in range(len(storage[0]) + 2)])

	for request in requests:
		if len(request) == 1:
			check_side(storage_list, request)

		else:
			for x in range(1, len(storage_list)-1):
				for y in range(1, len(storage_list[0])-1):
					if storage_list[x][y] == request[0]:
						storage_list[x][y] = '.'

	for x in range(1, len(storage_list)-1):
		for y in range(1, len(storage_list[0])-1):
			if not storage_list[x][y] == '.':
				answer += 1

	return answer


storage_input = ["AZWQY", "CAABX", "BBDDA", "ACACA"]
requests_input = ["A", "BB", "A"]

print(solution(storage_input, requests_input))