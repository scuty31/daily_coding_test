from collections import deque


def solution(queue1, queue2):
    answer = -1
    q1 = deque()
    q2 = deque()

    for i in range(len(queue1)):
        q1.append(queue1[i])
        q2.append(queue2[i])

    queue = deque()
    queue.append((sum(q1), sum(q2), q1, q2, 0))

    while queue:
        s1, s2, q1, q2, cnt = queue.popleft()

        if cnt >= len(queue1) * 2:
            break

        if s1 == s2:
            answer = cnt
            break

        fq1 = q1[0]
        fq2 = q2[0]





    return answer


queue1_input = [3, 2, 7, 2]
queue2_input = [4, 6, 5, 1]

#print(solution(queue1_input, queue2_input))