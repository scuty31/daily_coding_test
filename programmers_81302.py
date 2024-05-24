# 거리두기 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/81302

"""
코로나 바이러스 감염 예방을 위해 거리를 둬야 한다.
다음과 같은 규칙으로 대기실에 거리를 두고 앉도록 한다.

- 대기실은 5개이며, 5x5 크기이다.
- 응시자들 끼리는 맨해튼 거리가 2 이하로 앉지 않아야 한다.
- 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용한다.

각 대기실 별로 거리두기를 지키고 있으면 1, 지키지 않고 있으면 0을 배열에 담아 return 하여라.
"""



def bfs(place):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for r in range(5):
        for c in range(5):
            if place[r][c] == "P":
                v = [[False]*5 for _ in range(5)]
                v[r][c] = True
                q = [(r, c)]
                for _ in range(2):
                    tmp = []
                    for r, c in q:
                        for i in range(4):
                            rr, cc = r+dr[i], c+dc[i]
                            if 0 <= rr < 5 and 0 <= cc < 5:
                                if place[rr][cc] == 'X' or v[rr][cc]:
                                    continue
                                if place[rr][cc] == 'P':
                                    return 0
                                tmp.append((rr, cc))
                                v[rr][cc] = True
                    q = tmp
    return 1


def solution(places):
    return [bfs(place) for place in places]


places_ex = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places_ex))