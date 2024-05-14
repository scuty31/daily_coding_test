# 양과 늑대
# https://school.programmers.co.kr/learn/courses/30/lessons/92343

"""
문제 해석

2진 트리 모양 초원의 각 노드에 늑대와 양이 한 마리씩 놓여 있다.
각 노드를 방문할 때마다 해당 노드에 있던 양과 늑대가 따라오게 된다.
만약, 늑대의 수가 양의 수보다 크거나 같게 되면 늑대가 모든 양을 잡아먹는다.

양이 늑대에게 잡아먹히지 않도록 하면서 최대한 많은 수의 양을 모아서 다시 루트 노드로 돌아오려고 한다.
"""

"""
문제 접근

DFS 문제이다.
먼저, 양이 늑대보다 많으면 양의 수를 배열에 저장한다.
만약 양이 늑대보다 같거나 적으면 해당 과정을 끝낸다.

다음, 방문되지 않은 자식 노드가 있다면 자식노드로 이동한다.
이동 후, 양과 늑대 수를 업데이트한다.

이를 반복한다.
"""


def solution(info, edges):
    visited = [False] * len(info)
    answer = []

    # DFS 함수
    def dfs(sheep, wolf):
        # 만약 양의 수가 늑대 수보다 크다면
        if sheep > wolf:
            answer.append(sheep)
        else:
            return      # 양의 수가 늑대 수와 같거나 적다면 끝낸다.

        for p, c in edges:
            # 부모를 방문하고, 방문하지 않은 자식이 있다면
            if visited[p] and not visited[c]:
                visited[c] = True

                # 해당 칸에 양이 있다면 양의 수 + 1
                if info[c] == 0:
                    dfs(sheep + 1, wolf)
                # 해당 칸에 늑대가 있다면 늑대의 수 + 1
                else:
                    dfs(sheep, wolf + 1)

                # 탐색이 끝나면 되돌아가기
                visited[c] = False

    # 루트 노드부터 시작
    visited[0] = True
    dfs(1, 0)

    return max(answer)


info_ex = [0,0,1,1,1,0,1,0,1,0,1,1]
edges_ex = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

print(solution(info_ex, edges_ex))