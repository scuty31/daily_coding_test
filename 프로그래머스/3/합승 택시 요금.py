import heapq

INF = int(1e9)

def solution(n, s, a, b, fares):
    graphs = [[] for _ in range(n+1)]

    for i in range(len(fares)):
        left, right, v = fares[i]
        graphs[left].append((right, v))
        graphs[right].append((left, v))

    def dijkstra(start):
        dist = [INF] * (n+1)
        dist[start] = 0

        pq = [(0, start)]

        while pq:
            cost, now = heapq.heappop(pq)

            if cost > dist[now]:
                continue

            for nxt, fee in graphs[now]:
                new_cost = cost + fee

                if new_cost < dist[nxt]:
                    dist[nxt] = new_cost
                    heapq.heappush(pq, (new_cost, nxt))

        return dist

    dist_s = dijkstra(s)
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)

    answer = INF

    for k in range(1, n+1):
        cost = dist_s[k] + dist_a[k] + dist_b[k]
        answer = min(answer, cost)

    return answer


n_input = 7
s_input = 3
a_input = 4
b_input = 1
fares_input = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

print(solution(n_input, s_input, a_input, b_input, fares_input))