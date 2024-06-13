# 시소 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/152996


import math


def solution(weights):
    answer = 0
    weights_dict = dict()

    # 1m에 앉았을 때의 몸무게 구하기
    for i in range(len(weights)):
        weights[i] /= 2

        if weights_dict.get(weights[i]):
            weights_dict[weights[i]] += 1
        else:
            weights_dict[weights[i]] = 1

    weights_list = sorted(list(set(weights)))

    for value in weights_dict.values():
        answer += math.comb(value, 2)

    for i in range(len(weights_list) - 1):
        for j in range(i + 1, len(weights_list)):
            big = weights_list[j]
            small = weights_list[i]

            if big == small:
                answer += weights_dict[big] * weights_dict[small]
            elif big * 2 == small * 3:
                answer += weights_dict[big] * weights_dict[small]
            elif big == small * 2:
                answer += weights_dict[big] * weights_dict[small]
            elif big * 3 == small * 4:
                answer += weights_dict[big] * weights_dict[small]

    return answer


weights_ex = [100,180,360,100,270]

print(solution(weights_ex))