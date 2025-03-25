from collections import deque


def bfs(m, n, h, box, tomato):
    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    q = deque()
    visited = [[[False] * m for _ in range(n)] for _ in range(h)]

    for x, y, z in tomato:
        q.append((x, y, z))
        visited[z][x][y] = True

    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                continue
            if visited[nz][nx][ny]:
                continue
            if box[nz][nx][ny] == -1:
                continue

            if box[nz][nx][ny] == 0  or box[nz][nx][ny] > box[z][x][y] + 1:
                box[nz][nx][ny] = box[z][x][y] + 1
                visited[nz][nx][ny] = True
                q.append((nx, ny, nz))

    max_num = 0
    for iz in range(h):
        for ix in range(n):
            for iy in range(m):
               if box[iz][ix][iy] == 0:
                   return -1

               if box[iz][ix][iy] > max_num:
                   max_num = box[iz][ix][iy]

    return max_num - 1


def solution():
    m, n, h = map(int, input().split())
    box = []

    for i in range(h):
        box.append(list())
        for _ in range(n):
            box[i].append(list(map(int, input().split())))

    tomato = list()

    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    tomato.append((j, k, i))

    result = bfs(m, n, h, box, tomato)

    return result


print(solution())