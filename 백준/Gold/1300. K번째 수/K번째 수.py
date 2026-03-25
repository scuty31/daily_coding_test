def solution():
    n = int(input())
    k = int(input())

    left = 1
    right = k       # k 이상의 index는 나올 수가 없음
    answer = 0

    while left <= right:
        mid = (left+right)//2

        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid // i, n)

        if cnt >= k:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


print(solution())