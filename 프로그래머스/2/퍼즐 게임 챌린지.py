def calc(diffs, times, x):
    result = times[0]

    for i in range(1, len(diffs)):
        if diffs[i] <= x:
            result += times[i]
        else:
            result += (diffs[i] - x) * (times[i]+times[i-1]) + times[i]

    return result


def solution(diffs, times, limit):
    answer = 0
    left = 1
    right = max(diffs)

    while left <= right:
        mid = (left + right) // 2

        if calc(diffs, times, mid) <= limit:
            answer = mid
            right = mid-1
        else:
            left = mid + 1

    return answer


diff_input = [1, 328, 467, 209, 54]
times_input = [2, 7, 1, 4, 3]
limit_input = 1723

print(solution(diff_input, times_input, limit_input))