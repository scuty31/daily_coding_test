def solution():
    n = int(input())
    board = list()

    for _ in range(n):
        tmp = list(map(int, input().split()))

        board.append(tmp)

    visited = [[0] * n for _ in range(n)]
    visited[0][0] = 1

    dx = [0, 1]
    dy = [1, 0]

    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                continue

            for i in range(2):
                nx = x + (dx[i] * board[x][y])
                ny = y + (dy[i] * board[x][y])

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                visited[nx][ny] += visited[x][y]

    return visited[n-1][n-1]


print(solution())