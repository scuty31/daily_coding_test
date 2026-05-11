# 막대기
# https://www.acmicpc.net/problem/1094

"""
길이가 64cm인 막대를 Xcm로 만들려고 한다.
다음과 같은 방법으로 막대를 자르고 붙여 Xcm의 막대를 만들려고 한다.

- 가지고 있는 막대의 길이를 모두 더한다.
- 만약 합이 X보다 크면, 아래와 같은 과정을 반복한다.
    - 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
    - 만약, 자른 막대 중 하나를 버렸을 때의 길이의 합이 X보다 크거나 같다면 하나를 버린다.
- 남은 모든 막대를 풀로 붙여  Xcm를 만든다.

총 몇개의 막대를 붙여야 Xcm를 만들 수 있는지 구하여라.
"""

"""
처음에는 위의 조건에 맞게 코딩을 하였다.
가장 짧은 막대를 리스트의 마지막에 저장하여 구하였다.

하지만, 막대를 절반씩 잘라 X를 만드는 막대의 개수는 X를 2진수로 변환한 뒤,
1의 개수를 더한 것과 같다는 것을 알게 되었다.
이를 이용하여 문제를 푸니 더 적은 효율적이게 문제를 풀 수 있었다.
"""


"""
# 조건에 맞게 코딩

def solution():
    x = int(input())        # 구해야될 막대기의 총 길이
    sticks = [64]             # 붙힐 막대기

    if x == 64:
        return 1

    while True:
        # 가장 작은 막대기를 2등분
        stick = sticks.pop()
        stick //= 2

        # 하나만 넣고
        sticks.append(stick)

        # 전체 막대의 길이의 합이 x보다 작으면 나머지 막대기를 넣기
        if sum(sticks) < x:
            sticks.append(stick)
        # 같으면 나가기
        elif sum(sticks) == x:
            break

    return len(sticks)


print(solution())
"""


def solution():
    x = list(map(int, list(str(format(int(input()), 'b')))))

    return sum(x)


print(solution())
