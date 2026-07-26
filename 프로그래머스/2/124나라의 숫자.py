def solution(n):
    answer = ''
    num_list = []
    num = ['1', '2', '4']

    while n:
        n -= 1
        num_list.append(num[n%3])
        n //= 3

    answer = ''.join(list(reversed(num_list)))

    return answer


n_input = 10

print(solution(n_input))