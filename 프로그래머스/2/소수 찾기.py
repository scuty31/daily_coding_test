def check_num(number_list, number, level, visited, num):
    if level == len(number):
        return

    for i in range(len(number)):
        if visited[i]:
            continue

        if level == 0 and number[i] == '0':
            continue

        visited[i] = True
        num.append(number[i])

        number_list.add(int(''.join(num)))
        check_num(number_list, number, level+1, visited, num)

        visited[i] = False
        num.pop()


def check_prim(number_list, max_num):
    prim_list = [True for _ in range(max_num+1)]
    prim_list[0] = False
    prim_list[1] = False

    m = int(max_num ** 0.5)

    for i in range(2, m+1):
        if prim_list[i]:
            for j in range(i*i, max_num+1, i):
                prim_list[j] = False

    result = 0
    for num in number_list:
        if prim_list[num]:
            result += 1

    return result


def solution(numbers):
    answer = 0
    number_list = set()
    number = list(numbers)
    visited = [False for _ in range(len(number))]

    check_num(number_list, number, 0, visited, [])

    answer = check_prim(number_list, max(number_list))

    return answer


numbers_input = '011'

print(solution(numbers_input))