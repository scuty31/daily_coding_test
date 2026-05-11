# 두 원 사이의 정수의 쌍
# https://school.programmers.co.kr/learn/courses/30/lessons/181187


"""
2차원 직교 좌표계에 중심이 원점인 서로 다른 크기의 원이 2개 주어진다.
반지름을 나타내는 두 정수가 r1, r2라고 할 때, 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를 구하여라.
"""

"""
원을 4등분을 하여 한 조각 안에 있는 점의 개수를 구한 후, 4배를 하면 구할 수 있을 것이라 생각했다.
x좌표 기준으로 가능한 y좌표의 최대값 - 최솟값을 구하여 더한다.
만약 x좌표가 r1을 넘어가면  최댓값만 더한다.
"""

from math import ceil, floor, sqrt

def solution(r1, r2):
    answer = 0

    for i in range(r2):
        if i < r1:
            answer += (floor(sqrt(r2*r2 - i*i)) - ceil(sqrt(r1*r1 - i*i)) + 1)

        else:
            answer += (floor(sqrt(r2*r2 - i*i)))

    return answer * 4


r1_ex = 2
r2_ex = 3
print(solution(r1_ex, r2_ex))