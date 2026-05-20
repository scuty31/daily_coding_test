from collections import deque


def solution(s):
    s_list = deque()
    for i in range(len(s)):
        s_list.append(s[i])

    answer = 0
    x_count = 0
    y_count = 0
    x = ''

    while s_list:
        alpha = s_list.popleft()

        if x_count == y_count == 0:
            x = alpha
            x_count = 1
            continue

        if x == alpha:
            x_count += 1
        else:
            y_count += 1

        if x_count == y_count:
            x = ''
            answer += 1
            x_count = 0
            y_count = 0

    if x_count > 0:
        answer += 1

    return answer


input_s = "abracadabra"

print(solution(input_s))
