def check_star(stars, x, y, l):
	cnt = 0

	for sx, sy in stars:
		if x <= sx <= x+l and y <= sy <= y+l:
			cnt += 1

	return cnt


def solution():
	n, m, l, k = map(int, input().split())
	stars = list()
	result = 0

	for _ in range(k):
		x, y = map(int, input().split())
		stars.append((x, y))

	for i in range(k):
		for j in range(k):
			x = min(stars[i][0], stars[j][0])
			y = min(stars[i][1], stars[j][1])

			result = max(result, check_star(stars, x, y, l))

	print(k - result)


solution()




"""

"""