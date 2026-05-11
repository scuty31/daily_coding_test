from collections import deque


def bfs(maps, sx, sy, ex, ey):
	dx = [-1, 0, 1, 0]
	dy = [0, 1, 0, -1]

	visited = [[0 for _ in range(102)] for _ in range(102)]
	queue = deque()
	queue.append((sx, sy))
	visited[sx][sy] = 1

	while queue:
		x, y = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if nx < 0 or nx >= 102 or ny < 0 or ny >= 102:
				continue
			if maps[nx][ny] == 0 or maps[nx][ny] == 2:
				continue
			if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
				visited[nx][ny] = visited[x][y] + 1
				queue.append((nx, ny))

			if nx == ex and ny == ey:
				return visited[ex][ey]//2


def make_line(maps, rectangle):
	for lx, ly, rx, ry in rectangle:
		for x in range(lx, rx+1):
			for y in range(ly, ry+1):
				if x == lx or x == rx or y == ly or y == ry:
					if maps[x][y] == 0:
						maps[x][y] = 1
				else:
					maps[x][y] = 2



def solution(rectangle, characterX, characterY, itemX, itemY):
	answer = 0
	maps = [[0 for _ in range(102)] for _ in range(102)]

	for i in range(len(rectangle)):
		rectangle[i] = list(map(lambda x:x*2, rectangle[i]))

	characterX *= 2
	characterY *= 2
	itemX *= 2
	itemY *= 2

	make_line(maps, rectangle)
	answer = bfs(maps, characterX, characterY, itemX, itemY)

	return answer


rectangle_para = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX_para = 1
characterY_para = 3
itemX_para = 7
itemY_para = 8


print(solution(rectangle_para, characterX_para, characterY_para, itemX_para, itemY_para))

