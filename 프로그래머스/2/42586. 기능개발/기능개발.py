def solution(progresses, speeds):
    first_time = (100-progresses[0]) // speeds[0]
    if (100-progresses[0]) % speeds[0]:
        first_time += 1

    answer = [1]
    now_time = first_time

    for i in range(1, len(progresses)):
        need_time = ((100 - progresses[i]) // speeds[i])
        if (100-progresses[i]) % speeds[i]:
            need_time += 1

        if now_time < need_time:
            now_time = need_time
            answer.append(1)
        else:
            answer[-1] += 1

    return answer