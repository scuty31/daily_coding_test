# 혼자 놀기의 달인
# https://school.programmers.co.kr/learn/courses/30/lessons/131130


"""
문제 해석

숫자 카드 더미에 카드가 총 100장 있다.
카드에는 1부터 100까지 숫자가 하나씩 적혀있다.

범희는 다음과 같은 순서로 혼자 게임을 한다.
- 2 이상, 100 이하의 자연수를 하나 정한다.
- 그 수보다 작거나 같은 모든 숫자 카드들을 작은 상자에 따로 집어 넣는다.
- 무작위로 상자를 섞고 일렬로 나열한 후, 번호를 부여한다.
- 상자 하나를 무작위로 선택한다.
- 그 상자 안에 있는 숫자 카드가 적힌 상자를 선택한다.
- 숫자 카드가 적힌 상자가 열려있을 때까지 상자를 연다.
- 이렇게 연 상자들을 1번 상자 그룹으로 묶는다.
- 남은 상자들을 이용하여 2번 상자 그룹을 만든다.
- 1번 상자 그룹에 속한 상자의 개수와 2번 상자 그룹에 속한 상자의 개수를 곱하여 점수를 낸다.
- 만약 2번 상자 그룹을 만들 수 없다면 점수는 0점이 된다.

무작위로 상자를 섞고 일렬로 나열했을 때의 상자 배열이 매개변수로 주어질 때, 얻을 수 있는 최고 점수를 구하여라.
"""

"""
문제 접근

상자의 개수가 최대 100개이기 때문에 각 상자에서부터 시작하여 상자 그룹을 만들어 본다.
각 상자에서부터 시작한 상자 그룹에 속한 상자의 개수를 리스트에 저장한다.

점수가 최대가 되는 경우는 2개이다.
- 상자의 개수가 가장 많은 그룹이 2개 이상일 때
- 상자의 개수가 가장 많은 그룹이 1개일때

상자의 개수가 가장 많은 그룹이 2개 이상이면 가장 많은 개수를 2번 곱하여 최대 점수를 구할 수 있다.
상자의 개수가 가장 많은 그룹이 1개라면 가장 많은 개수와 2번째로 많은 개수를 구한 후, 서로 곱하여 최대 점수를 구할 수 있다.
"""


def solution(cards):
    # 다음 상자 번호가 적힌 딕셔너리
    card_dict = {i: cards[i - 1] for i in range(1, len(cards) + 1)}
    # 해당 위치의 상자 개수
    card_cnt = [0] * (len(cards) + 1)

    # 상자 그룹을 구성하고 상자 개수 구하기
    for i in range(1, len(cards) + 1):
        visited = [False] * (len(cards) + 1)
        visited[i] = True
        n = card_dict[i]
        card_cnt[i] = 1

        while True:
            if visited[n]:
                break

            visited[n] = True
            n = card_dict[n]
            card_cnt[i] += 1

    max_card_cnt = max(card_cnt)

    # 상자의 개수가 가장 많은 그룹이 2개 이상일 때
    if max_card_cnt != card_cnt.count(max_card_cnt):
        answer = max_card_cnt * max_card_cnt

    # 상자의 개수가 가장 많은 그룹이 1개일 때
    else:
        answer = max_card_cnt
        next_card_cnt = 0       # 2번째로 많은 개수의 상자가 있는 그룹에 속한 상자의 개수

        for i in range(len(card_cnt)):
            if card_cnt[i] == max_card_cnt:
                continue
            next_card_cnt = max(next_card_cnt, card_cnt[i])

        answer *= next_card_cnt

    return answer


cards_ex = [8, 6, 3, 7, 2, 5, 1, 4]
print(solution(cards_ex))
