def solution():
	n = int(input())
	m = int(input())
	x = list(map(int, input().split()))
	answer = max(x[0], n - x[-1])

	for i in range(1, len(x)):
		d = (x[i] - x[i-1])//2
		if (x[i] - x[i-1]) % 2 != 0:
			d += 1

		answer = max(answer, d)

	return answer


print(solution())