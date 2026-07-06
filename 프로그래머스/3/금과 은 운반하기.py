def solution(a, b, g, s, w, t):
    answer = -1

    left = 0
    right = 4*10**14

    while left <= right:
        mid = (left + right) // 2
        gold, silver, total = 0, 0, 0

        for i in range(len(g)):
            count = mid // (2 * t[i])
            if mid % (2*t[i]) >= t[i]:
                count += 1

            move = count * w[i]

            gold += min(g[i], move)
            silver += min(s[i], move)
            total += min(g[i] + s[i], move)

        if gold >= a and silver >= b and total >= a+b:
            answer = mid
            right = mid - 1
        else:
            left = mid +1

    return answer


a_input = 10
b_input = 10
g_input = [100]
s_input = [100]
w_input = [7]
t_input = [10]

print(solution(a_input, b_input, g_input, s_input, w_input, t_input))