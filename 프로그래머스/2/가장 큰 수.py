def solution(numbers):
    answer = ''
    numbers_max_len = 0
    numbers = list(map(str, numbers))
    numbers_sort_list = []

    for i in range(len(numbers)):
        numbers_max_len = max(numbers_max_len, len(numbers[i]))

    for i in range(len(numbers)):
        numbers_sort_list.append((numbers[i]*numbers_max_len, i))

    numbers_sort_list.sort(reverse=True)

    for _, idx in numbers_sort_list:
        answer += str(numbers[idx])

    if len(answer) == answer.count('0'):
        answer = '0'

    return answer


numbers_input = [3, 30, 345, 5, 9]
print(solution(numbers_input))