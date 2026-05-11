def solution():
	n = int(input())
	cost = list(map(int, input().split()))
	total = int(input())

	if sum(cost) <= total:
		return max(cost)

	low, high = 0, max(cost)
	answer = 0

	while low <= high:
		mid = (low + high) // 2
		total_cost = sum(min(mid, c) for c in cost)

		if total_cost > total:
			high = mid - 1
		else:
			low = mid + 1
			answer = mid

	return answer


print(solution())