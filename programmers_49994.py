# 방문 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/49994

"""
캐릭터를 4가지 명령을 통해 움직이려고 한다.
- U : 위쪽으로 한 칸 가기
- D : 아래쪽으로 한 칸 가기
- R : 오른쪽으로 한 칸 가기
- L : 왼쪽으로 한 칸 가기

캐릭터는 (0, 0) 위치에서 시작한다.
맵은 좌표평면 -5 ~ 5까지 존재한다.

캐릭터가 명령어대로 움직였을 때, 처음 걸어본 길의 길이를 구하여라.
"""

"""
맵의 크기를 0~10으로 맞춘다.
캐릭터의 처음 위치를 (5, 5)로 지정한다.
해당 위치에서 명령어대로 움직이게 한다.
움직일 때마다 이동한 길을 표시한다.
만약, 캐릭터가 이동했던 길을 한번 더 이동할 때는 count하지 않는다.

총 visited의 개수를 4개를 만들어 해당 점에서 위, 아래, 오른쪽, 왼쪽으로 이동할 때마다 표시하도록 한다.
"""
def move(dirs, player, visited):
    cnt = 0
    d_dict = {"U": 0, "D": 1, "R": 2, "L": 3}       # 순서대로 위, 아래, 오른쪽, 왼쪽
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    x, y = player

    # 각 명령어를 수행한다.
    for d_str in dirs:
        # 명령어에 맞게 이동한다.
        d = d_dict[d_str]
        nx = x + dx[d]
        ny = y + dy[d]

        # 맵 밖으로 나가야 한다면 명령어를 무시한다.
        if nx < 0 or ny < 0 or nx >= 11 or ny >= 11:
            continue

        # 처음 가보는 길이면 추가한다.
        if visited[d][nx][ny] == 0:
            visited[d][nx][ny] = 1
            cnt += 1

        x, y = nx, ny

    return cnt


def solution(dirs):
    player = (5, 5)     # 플레이어는 (0, 0)에 있다.
    visited = [[[0] * 11 for _ in range(11)] for _ in range(4)]     # 총 맵은 -5부터 5까지 있다.

    answer = move(dirs, player, visited)

    return answer


dirs_ex = "LULLLLLLU"
print(solution(dirs_ex))