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
캐릭터가 명령어를 수행할 때, 명령어를 수행하기 전의 좌표와 명령어를 수행한 후의 좌표를 기록한다.
만약 명령어를 수행할 수 없으면 넘어간다.
출발 좌표와 도착 좌표가 같다면 해당 길은 이미 걸어본 길이기 때문에 count를 하지 않는다.
"""

def solution(dirs):
    x, y = 0, 0     # 플레이어는 (0, 0)에 있다.
    d_dict = {"U": 0, "R": 1, "D": 2, "L": 3}  # 순서대로 위, 오른쪽, 아래, 왼쪽
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = []
    answer = 0

    # 각 명령어를 수행한다.
    for d_str in dirs:
        # 명령어에 맞게 이동한다.
        d = d_dict[d_str]
        nx = x + dx[d]
        ny = y + dy[d]

        # 맵 밖으로 나가야 한다면 명령어를 무시한다.
        if nx < -5 or ny < -5 or nx > 5 or ny > 5:
            continue

        # 처음 가보는 길이면 추가한다.
        if (x, y, nx, ny) not in visited:
            visited.append((x, y, nx, ny))
            visited.append((nx, ny, x, y))
            answer += 1

        # 이동한다.
        x = nx
        y = ny

    return answer


dirs_ex = "ULURRDLLU"
print(solution(dirs_ex))