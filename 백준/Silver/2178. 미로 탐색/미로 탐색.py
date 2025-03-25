from collections import deque


def escape(n, m, maze):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    visited = [[0] * m for _ in range(n)]

    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue

            if visited[nx][ny] == 0 or visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y]  + 1
                q.append((nx, ny))

                if nx == n-1 and ny == m-1:
                    return visited[nx][ny]

    return visited[n-1][m-1]



def solution():
    n, m = map(int, input().split())
    maze = list()

    for _ in range(n):
        maze.append(list(map(int, list(input()))))

    result = escape(n, m, maze)

    return result


print(solution())