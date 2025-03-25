from collections import deque


def check(n, maps, sx, sy, s_size):
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 9:
                continue
            if maps[i][j] != 0:
                return True

    return False


def move(n, maps, sx, sy, s_size, s_count):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque()
    visited = [[-1] * n for _ in range(n)]
    visited[sx][sy] = 0
    q.append((sx, sy))
    answer = list()

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if maps[nx][ny] > s_size:
                continue
            if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

                if maps[nx][ny] != 0 and maps[nx][ny] < s_size:
                    n_count = s_count + 1
                    n_size = s_size

                    if n_count == n_size:
                        n_size += 1
                        n_count = 0

                    answer.append([nx, ny, n_size, n_count, visited[nx][ny]])

    if answer:
        answer.sort(key=lambda x : (x[-1], x[0], x[1]))
        result = answer[0]

        maps[result[0]][result[1]] = 0

        return answer[0]

    return -1, -1, -1, -1, -1


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

    while check(n, maps, sx, sy, s_size):
        sx, sy, s_size, s_count, time_count = move(n, maps, sx, sy, s_size, s_count)

        if sx == -1 and sy == -1:
            break

        now_time += time_count

    return now_time


print(solution())