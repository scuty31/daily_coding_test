# 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

"""
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶어한다.
Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 다음과 같이 섞어 새로운 음식을 만들려고 한다.
- 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞는다.
섞어야 하는 최소 횟수를 구하여라.
"""

"""
최소 힙을 이용한다.
최소 힙에서 원소 하나를 뽑았을 때, K 미만이라면 하나를 더 뽑아 섞고 count를 1개 증가시킨다.
K 이상이 되면 count를 반환한다. 
"""
import heapq


def solution(scoville, K):
    q = []
    answer = 0

    # 최소 힙에 스코빌 지수 저장
    heapq.heapify(scoville)

    # 스코빌 지수를 비교하고 섞는다.
    while True:
        min_scoville = heapq.heappop(scoville)  # 가장 맵지 않은 음식의 스코빌 지수

        # 가장 맵지 않은 음식의 스코빌 지수가 K보다 크다면 섞는 것을 그만둔다.
        if min_scoville >= K:
            break

        # 더이상 스코빌 지수를 K 이상 만들 수 없다면 그만둔다.
        if len(scoville) == 0:
            answer = -1
            break

        second_min_scoville = heapq.heappop(scoville)  # 두 번째로 맵지 않은 음식의 스코빌 지수

        # 섞은 스코빌 지수를 다시 최소 힙에 저장
        heapq.heappush(scoville, min_scoville + (second_min_scoville * 2))
        answer += 1  # count 증가

    return answer


scoville_ex = [1, 2, 3, 9, 10, 12]
k_ex = 7

print(solution(scoville_ex, k_ex))