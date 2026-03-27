from collections import deque


def solution():
    n, k = map(int, input().split())

    if n == k:
        print(0)
        print(1)
        return

    q = deque([n])
    dist = [-1] * 100001
    cnt = [0] * 100001

    dist[n] = 0
    cnt[n] = 1

    while q:
        now_loc = q.popleft()

        for next_loc in (now_loc-1, now_loc+1, now_loc*2):
            if 0 <= next_loc <= 100000:
                if dist[next_loc] == -1:                    # 만약 처음 간 경우
                    dist[next_loc] = dist[now_loc] + 1      # 거리 + 1
                    cnt[next_loc] = cnt[now_loc]            # 해당 거리까지의 경우의 수는 동일
                    q.append(next_loc)

                elif dist[next_loc] == dist[now_loc]+1:       # 만약 이전에 간 경우 중 거리가 같다면
                    cnt[next_loc] += cnt[now_loc]           # 해당 거리까지의 경우의 수에 현재 거리까지의 경우의 수 합치기

    print(dist[k])
    print(cnt[k])


solution()