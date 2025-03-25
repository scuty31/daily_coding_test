from collections import deque


def move(n, maps, sx, sy, s_size, s_count):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque()
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    q.append((sx, sy, 0))
    answer = list()
    min_distance = int(1e9)

    while q:
        x, y, dist = q.popleft()

        if dist > min_distance:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if maps[nx][ny] > s_size:
                continue

            visited[nx][ny] = True
            n_dist = dist + 1

            if 0 < maps[nx][ny] < s_size:
                if n_dist < min_distance:
                    min_distance = n_dist
                    answer = [[nx, ny]]

                elif n_dist == min_distance:
                    answer.append([nx, ny])

            q.append((nx, ny, n_dist))

    if not answer:
        return -1, -1, -1, -1, -1

    answer.sort(key=lambda x: (x[0], x[1]))

    sx, sy = answer[0]
    maps[sx][sy] = 0
    s_count += 1

    if s_count == s_size:
        s_size += 1
        s_count = 0

    return sx, sy, s_size, s_count, min_distance


def solution():
    n = int(input())
    maps = list()

    for _ in range(n):
        maps.append(list(map(int, input().split())))

    sx, sy = -1, -1                   # 아기 상어의 위치
    s_size = 2
    s_count = 0
    now_time = 0
    time_count = 0

    for i in range(n):
        for j in range(n):
            if maps[i][j] == 9:
                sx = i
                sy = j
                maps[i][j] = 0
                break
        if sx != -1 and sy != -1:
            break

    while True:
        sx, sy, s_size, s_count, time_count = move(n, maps, sx, sy, s_size, s_count)

        if sx == -1 and sy == -1:
            break

        now_time += time_count

    return now_time


print(solution())