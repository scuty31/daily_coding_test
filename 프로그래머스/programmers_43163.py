# 단어 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

"""
두 개의 단어 begin, target과 단어의 집합 words가 있다.
아래 규칙을 이용해서 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 한다.
- 한 번에 한 개의 알파벳만 바꿀 수 있다.
- words에 있는 단어로만 변환할 수 있다.

최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return하여라.
"""

"""
각 단어에서 변환할 수 있는 단어의 index를 구한다.
begin에서 시작하여 target인 index까지 도달할 수 있는지 확인한다. 
"""

from collections import deque


# 너비 우선 탐색을 이용하여 target으로 변환할 수 있는지 확인하는 함수
def bfs(start, target, words, graph):
    visited = [-1] * len(words)
    q = deque()

    q.append(start)
    visited[start] = 0

    while q:
        word_idx = q.popleft()

        # 현재 단어에서 변환할 수 있는 모든 단어를 확인
        for n in graph[word_idx]:
            if visited[n] == -1 or visited[n] > visited[word_idx] + 1:
                q.append(n)
                visited[n] = visited[word_idx] + 1

                # target으로 변환하면 return
                if words[n] == target:
                    return visited[n]

    return 0


def solution(begin, target, words):
    # target으로 변환할 수 없다면
    if target not in words:
        return 0

    # 변환할 수 있는 index 탐색
    graph = [[] for _ in range(len(words) + 1)]
    words.insert(0, begin)

    for i in range(len(words) - 1):
        for j in range(i+1, len(words)):
            # 두 단어의 다른 알파벳이 1개라면 graph에 index 저장
            for k in range(len(words[i])):
                tmp_list_1 = list(words[i])
                tmp_list_2 = list(words[j])
                tmp_list_1.pop(k)
                tmp_list_2.pop(k)

                tmp_1 = ''.join(tmp_list_1)
                tmp_2 = ''.join(tmp_list_2)

                if tmp_1 == tmp_2:
                    graph[i].append(j)
                    graph[j].append(i)
                    break

    answer = bfs(0, target, words, graph)

    return answer


begin_ex = 'aoa'
target_ex = 'aof'
words_ex = ["aob", "aoc", "aod", "aof", "aoe"]

print(solution(begin_ex, target_ex, words_ex))