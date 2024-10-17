import heapq


def dijkstra(n, graph, start):
	q = []
	distance = [int(1e9) for _ in range(n+1)]
	heapq.heappush(q, (0, start))
	distance[start] = 0

	while q:
		dist, node = heapq.heappop(q)

		if distance[node] < dist:
			continue

		for now_node, now_dist in graph[node]:
			cost = dist + now_dist

			if distance[now_node] > cost:
				heapq.heappush(q, (cost, now_node))
				distance[now_node] = cost

	return distance[n]


def solution():
	n, m = map(int, input().split())
	graph = [[] for _ in range(n+1)]

	for _ in range(m):
		s, e, v = map(int, input().split())
		graph[s].append((e, v))
		graph[e].append((s, v))

	answer = dijkstra(n, graph, 1)

	return answer


print(solution())