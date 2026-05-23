def solution(array):
    answer = []

    answer.append(max(array))
    answer.append(array.index(answer[-1]))

    return answer