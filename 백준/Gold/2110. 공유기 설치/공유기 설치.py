def check(house_list, mid, c):
    now_wifi = house_list[0]
    cnt = 1

    for i in range(1, len(house_list)):
        if house_list[i] - now_wifi >= mid:
            now_wifi = house_list[i]
            cnt += 1

    return cnt >= c


def solution():
    n, c = map(int, input().split())
    house_list = sorted(list(int(input()) for _ in range(n)))

    left = 1
    right = house_list[-1] - house_list[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if check(house_list, mid, c):
            answer = mid
            left = mid + 1

        else:
            right = mid - 1

    return answer


print(solution())