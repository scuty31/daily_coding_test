# 이중우선순위큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

"""
문제 해석

이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조이다.
- I 숫자 : 큐에 주어진 숫자를 삽입한다.
- D 1 : 큐에서 최댓값을 삭제한다.
- D -1 : 큐에서 최솟값을 삭제한다.

이중 우선순위 큐가 할 연산 operations가 매개변수로 주어진다.
모든 연산을 처리한 후, 큐가 비어있으면 [0, 0]을 출력하고,
큐가 비어있지 않으면 [최댓값, 최솟값]을 return하여라.
"""

"""
문제 접근

2개의 우선순위 큐를 만든다.
하나에는 최댓값을 뽑아내고, 다른 하나에는 최솟값을 뽑아낸다.
숫자가 들어올 때마다 count하여 현재 queue에 들어있어야 하는 숫자의 갯수를 구한다.
딕셔너리에 숫자를 기록하여 현재 queue에 어떤 숫자가 들어있는지 확인할 수 있도록 한다.

operations를 탐색하면서 숫자를 삽입하고, 삭제한다.
삽입할 때는 2개의 우선순위 큐에 동시에 삽입한다.
삭제할 때는 해당하는 우선순위 큐에서만 삭제하고, 딕셔너리에서 해당 수의 value를 0으로 만든다.

queue가 비었는지 빠르게 확인하기 위해 count를 사용한다.
queue에 숫자가 있다면 딕셔너리를 탐색하여 value가 1인 숫자들 중 최댓값과 최솟값을 찾는다.
"""
import heapq


def solution(operations):
    answer = []
    max_queue = []
    min_queue = []
    num_cnt = 0
    num_dict = dict()

    for operation in operations:
        # 명령어, 데이터 나누기
        op, num = operation.split()

        # 삽입하는 명령어라면
        if op == 'I':
            heapq.heappush(min_queue, int(num))
            heapq.heappush(max_queue, -int(num))
            num_cnt += 1
            num_dict[int(num)] = 1

        # 삭제하는 명령어라면
        else:
            if num == '1':
                if num_cnt:
                    n = heapq.heappop(max_queue)
                    num_cnt -= 1
                    num_dict[-n] = 0

            else:
                if num_cnt:
                    n = heapq.heappop(min_queue)
                    num_cnt -= 1
                    num_dict[n] = 0


    # 남아있는 수가 있다면
    if num_cnt:
        num_list = []

        for key, value in num_dict.items():
            if value:
                num_list.append(key)

        answer.append(max(num_list))
        answer.append(min(num_list))

    # 남아있는 수가 없다면
    else:
        answer.append(0)
        answer.append(0)

    return answer


operations_ex = ["I 1", "I 2", "D 1", "D -1", "I 3", "I 4", "D 1"]

print(solution(operations_ex))