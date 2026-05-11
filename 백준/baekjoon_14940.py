# 쉬운 최단거리
# https://www.acmicpc.net/problem/14940


from collections import deque


def bfs(maps, x, y, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return visited


def solution():
    n, m = map(int, input().split())
    maps = []

    for _ in range(n):
        maps.append(list(map(int, input().split())))

    x, y = -1, -1

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                x = i
                y = j
                break

        if x != -1 and y != -1:
            break

    answer = bfs(maps, x, y, n, m)

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                answer[i][j] = 0

        print(' '.join(list(map(str, answer[i]))))


solution()