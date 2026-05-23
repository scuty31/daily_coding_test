def solution(array):
    answer = []

    answer.append(max(array))
    answer.append(array.index(answer[-1]))

    return answer


array_input = [9, 10, 11, 8]

print(solution(array_input))