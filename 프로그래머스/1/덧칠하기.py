def solution(n, m, section):
    answer = 0
    painted = 0

    for s in section:
        if s > painted:
            painted = s+m-1
            answer += 1

    return answer


input_n = 8
input_m = 4
input_section = [2, 3, 6]

print(solution(input_n, input_m, input_section))