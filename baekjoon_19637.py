def check_stats(stats_list, stats):
	s, e = 0, len(stats_list) - 1

	while s <= e:
		mid = (s+e)//2

		if stats_list[mid] <= stats < stats_list[mid+1]:
			return mid




def solution():
	char_dic = dict()
	stats_list = [0]
	n, m = map(int, input().split())

	for _ in range(n):
		word, stats = input().split()

		if not char_dic.get(int(stats)):
			char_dic[int(stats)] = word
			stats_list.append(int(stats))




solution()