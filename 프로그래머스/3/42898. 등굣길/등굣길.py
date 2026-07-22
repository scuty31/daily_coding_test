from collections import deque


def bfs(m, n, board):
    queue = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue.append((0, 0))
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(1, 0), (0, 1)]:
            nx = x + dx
            ny = y + dy

            if nx >= n or ny >= m:
                continue
            if visited[nx][ny] != 0:
                visited[nx][ny] += visited[x][y]
                continue
            if board[nx][ny] == 1:
                continue

            visited[nx][ny] += visited[x][y]
            queue.append((nx, ny))

    return visited[n-1][m-1]


def solution(m, n, puddles):
    answer = 0
    board = [[0 for _ in range(m)] for _ in range(n)]

    for x, y in puddles:
        board[y-1][x-1] = 1

    answer = bfs(m, n, board)


    return answer % 1000000007