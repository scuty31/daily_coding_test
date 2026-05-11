def check_len(str_list, n, idx, s):
	cnt = 0
	str_len = 0

	while idx < len(str_list):
		if str_list[idx] == s:
			cnt += 1

		str_len += 1
		idx += 1

		if cnt == n:
			return str_len

	return 0


def solution():
	str_list = list(input())
	n = int(input())
	str_dict = dict()
	str_len = []

	for s in str_list:
		if str_dict.get(s):
			str_dict[s] += 1
		else:
			str_dict[s] = 1

	for i in range(len(str_list)):
		if str_dict[str_list[i]] < n:
			continue

		now_len = check_len(str_list, n, i, str_list[i])

		if now_len:
			str_len.append(now_len)

	if len(str_len):
		print(min(str_len), max(str_len))
	else:
		print(-1)


t = int(input())

for _ in range(t):
	solution()