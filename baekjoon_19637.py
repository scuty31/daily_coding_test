import sys


def check_stats(stats_list, stats):
	low = 0
	high = len(stats_list)
	result = 0

	while low <= high:
		mid = (low + high) // 2

		if stats_list[mid] >= stats:
			result = mid
			high = mid - 1
		else:
			low = mid + 1

	return stats_list[result]


def solution():
	n, m = map(int, sys.stdin.readline().split())
	style_dic = dict()
	stats_list = []

	for _ in range(n):
		style, stats = sys.stdin.readline().split()

		if style_dic.get(int(stats)):
			continue

		style_dic[int(stats)] = style
		stats_list.append(int(stats))

	stats_list.sort()

	for _ in range(m):
		char_stats = int(sys.stdin.readline().strip())
		result = check_stats(stats_list, char_stats)
		print(style_dic[result])


solution()