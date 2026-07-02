def set_number(n, k):
    answer = ''

    while n:
        answer += str(n%k)
        n //= k

    return answer[::-1]


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number**(1/2))+1):
        if number % i == 0:
            return False

    return True


def solution(n, k):
    answer = 0
    number = set_number(n, k)
    number_arr = number.split('0')

    for num in number_arr:
        if num == '':
            continue

        if is_prime(int(num)):
            answer += 1

    return answer


n_input = 110011
k_input = 10

print(solution(n_input, k_input))