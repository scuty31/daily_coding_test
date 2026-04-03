import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, trust_list, n):
    # 각 BFS 실행마다 visited 배열 초기화
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True

    count = 1  # 시작 컴퓨터를 포함하여 카운트 시작

    while q:
        node = q.popleft()

        # 현재 노드를 신뢰하는 모든 컴퓨터 확인
        for next_node in trust_list[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
                count += 1  # 해킹된 컴퓨터 수 증가

    return count


def solution():
    n, m = map(int, input().split())
    trust_list = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        # A가 B를 신뢰한다면, B를 해킹하면 A도 해킹할 수 있음
        trust_list[b].append(a)

    max_hacked = 0
    result = []

    # 모든 컴퓨터에서 BFS 실행
    for i in range(1, n + 1):
        hacked_count = bfs(i, trust_list, n)

        # 새로운 최댓값을 찾으면 max_hacked를 업데이트하고 결과 리스트 초기화
        if hacked_count > max_hacked:
            max_hacked = hacked_count
            result = [i]
        # 현재 최댓값과 같다면 결과 리스트에 추가
        elif hacked_count == max_hacked:
            result.append(i)

    # 결과를 공백으로 구분하여 출력
    print(*(result))


solution()