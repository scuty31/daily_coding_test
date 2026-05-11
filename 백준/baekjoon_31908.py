# 커플링 매치
# https://www.acmicpc.net/problem/31908

"""
커플은 왼손 약지에 남들과 구별되는 반지름 커플링을 착용한다.
모든 재학생의 왼속 약지를 확인하여 특징이 같은 반지를 착용한 사람이 2명이라면 커플이라고 판단한다.
커플이 누구인지 확인하여라.
"""

"""
반지의 특성을 key로, 사람 이름이 들어간 리스트를 value로 가지는 딕셔너리를 선언한다.
반지가 있다면 해당 반지의 특성을 딕셔너리에 추가한다.
만약 해당 반지를 끼고 있는 사람이 2명이라면 해당되는 두 사람을 커플로 지정한다.
"""

def solution():
    answer = []
    n = int(input())
    ring_dict = dict()
    ring_info = []

    for _ in range(n):
        ring_info.append(list(input().split()))

    # 사람들의 약지를 확인한다.
    for name, ring in ring_info:
        # 약지에 반지가 없다면 넘어간다.
        if ring == '-':
            continue

        # 반지가 딕셔너리에 있다면 이름을 추가한다.
        if ring_dict.get(ring):
            ring_dict[ring].append(name)

        # 반지가 딕셔너리에 없다면 새로 추가한다.
        else:
            ring_dict[ring] = [name]

    for ring, name in ring_dict.items():
        if len(name) == 2:
            answer.append(name)

    return answer


result = solution()

print(len(result))

for i in range(len(result)):
    print(' '.join(result[i]))