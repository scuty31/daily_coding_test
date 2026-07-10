def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i

    return result


def solution(n, k):
    answer = []
    lines = []

    for i in range(1, n + 1):
        lines.append(i)

    k -= 1

    while lines:
        n -= 1
        group_size = factorial(n)
        idx = k // group_size
        answer.append(lines.pop(idx))
        k %= group_size

    return answer


n_input = 3
k_input = 5

print(solution(n_input, k_input))