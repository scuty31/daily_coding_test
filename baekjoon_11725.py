# 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

"""
루트가 1인 트리가 주어진다.
각 노드의 부모를 구하여라.
"""

"""
각 노드를 돌면서 한 노드에서 다른 노드로 이동할 수 있다면,
이동할 수 있는 노드들의 부모는 이 노드가 된다.
이를 이용하여 부모를 구하고 딕셔너리에 저장한다.

최종적으로 딕셔너리에 저장되어 있는 부모를 2번 노드부터 순서대로 출력한다.
"""

from collections import deque


def bfs(graph, node_dict):
    q = deque()
    visited = [0 for _ in range(len(graph))]

    q.append(1)
    visited[1] = 1
    x = 1

    while q:
        x = q.popleft()

        for node in graph[x]:
            if visited[node]:
                continue

            node_dict[node] = x
            q.append(node)
            visited[node] = 1

    return


def solution():
    n = int(input())
    graph = [[] for _ in range(n+1)]
    node_dict = {i: 0 for i in range(1, n+1)}

    for _ in range(n-1):
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    bfs(graph, node_dict)

    for i in range(2, n+1):
        print(node_dict[i])


solution()