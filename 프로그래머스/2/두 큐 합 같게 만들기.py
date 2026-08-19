def solution(queue1, queue2):
    answer = -1
    q1 = queue1 + queue2
    q2 = queue2 + queue1
    cnt = 0
    q1_idx = 0
    q2_idx = 0
    q1_sum, q2_sum = sum(queue1), sum(queue2)

    while cnt <= len(q1)*2:
        if q1_sum == q2_sum:
            answer = cnt
            break

        if q1_idx < len(q1) and q1_sum > q2_sum:
            if q1_idx != len(q1):
                q1_sum -= q1[q1_idx]
                q2_sum += q1[q1_idx]
                q1_idx += 1

        elif q2_idx < len(q2) and q1_sum < q2_sum:
            if q2_idx != len(q2):
                q1_sum += q2[q2_idx]
                q2_sum -= q2[q2_idx]
                q2_idx += 1

        cnt += 1

    return answer


queue1_input = [3, 2, 7, 2]
queue2_input = [4, 6, 5, 1]

print(solution(queue1_input, queue2_input))