from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque()

    for i in range(len(priorities)):
        queue.append((i, priorities[i]))

    sort_priority = sorted(priorities)

    while True:
        if queue[0][1] == sort_priority[-1]:
            idx, _ = queue.popleft()
            sort_priority.pop()
            answer += 1

            if location == idx:
                return answer

        else:
            queue.append((queue.popleft()))

    return answer


priorities_input = [1, 1, 9, 1, 1, 1]
location_input = 0

print(solution(priorities_input, location_input))