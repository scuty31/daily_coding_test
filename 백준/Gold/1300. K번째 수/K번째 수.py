def solution():
    n = int(input())
    k = int(input())

    left = 1
    right = k       # k 이상의 index는 나올 수가 없음
    answer = 0

    while left <= right:
        mid = (left+right)//2

        cnt = 0     # mid에 해당하는 숫자 앞에 존재하는 모든 수의 개수
        for i in range(1, n+1):
            cnt += min(mid // i, n)     # i번째 행에서 mid 이하인 숫자의 개수, 각 행의 최대 원소의 개수 = n

        if cnt >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


print(solution())