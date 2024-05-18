# 미로 탈출
# https://school.programmers.co.kr/learn/courses/30/lessons/159993


"""
문제 해석

직사각형 격자 형태의 미로에서 탈출을 하려고 한다.
각 칸은 통로 또는 벽으로 구성되어 있으며, 벽으로 된 칸은 지나갈 수 없다.
탈출구는 1개만 존재하며, 레버를 당겨서만 열 수 있다.
레버 역시, 미로 내에 있다.
레버를 당기지 않아도 탈출구는 통과할 수 있다.

각 칸을 이동할 때 1초가 걸린다면, 탈출할 수 있는 최소 시간을 구하여라.
"""

"""
문제 접근

시작 지점에서 레버까지의 최소 거리를 구한다.
레버에서부터 탈출구까지의 최소 거리를 구한다.
두 거리를 더한다.
만약, 둘 중 한 곳이라도 도달할 수 없다면 -1을 출력한다.
"""


from collections import deque


def find_exit(maps, x, y, ex, ey):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    visited = [[0] * m for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q.append((x, y, 0))
    visited[x][y] = 1

    while q:
        x, y, cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 'X':
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = 1
            q.append((nx, ny, cnt + 1))

            if nx == ex and ny == ey:
                return cnt + 1

    return -1


def solution(maps):
    x = 0  # 시작 지점의 x좌표
    y = 0  # 시작 지점의 y좌표
    ex = 0  # 출구의 x좌표
    ey = 0  # 출구의 y좌표
    lx = 0  # 레버의 x좌표
    ly = 0  # 레버의 y좌표

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                x = i
                y = j

            elif maps[i][j] == 'L':
                lx = i
                ly = j

            elif maps[i][j] == 'E':
                ex = i
                ey = j

    l_cnt = find_exit(maps, x, y, lx, ly)

    if l_cnt == -1:
        return -1

    e_cnt = find_exit(maps, lx, ly, ex, ey)

    if e_cnt == -1:
        return -1

    return l_cnt + e_cnt