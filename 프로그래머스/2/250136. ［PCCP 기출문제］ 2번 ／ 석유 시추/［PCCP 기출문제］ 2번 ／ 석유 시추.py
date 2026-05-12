from collections import deque


def bfs(land, n, m, visited, x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    count = 0
    columns = set()

    while q:
        x, y = q.popleft()
        count += 1
        columns.add(y)

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if land[nx][ny] == 0:
                continue

            if visited[nx][ny] == 1:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny))

    return count, columns


def solution(land):
    n = len(land)
    m = len(land[0])
    oil_list = [0] * m
    visited = [[0] * len(land[0]) for _ in range(len(land))]

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                oil_count, columns = bfs(land, n, m, visited, i, j)

                for col in columns:
                    oil_list[col] += oil_count

    return max(oil_list)