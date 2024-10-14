def solution():
	n = list(input())
	num_list = [['']]

	idx = 1
	num_list.append(list(str(idx)))

	for num in n:

		while True:
			if num in num_list[idx]:
				for _ in range(len(num_list[idx])):
					if num == num_list[idx][0]:
						num_list[idx].pop(0)
						break

					num_list[idx].pop(0)
				break

			else:
				idx += 1
				num_list.append(list(str(idx)))

	return idx


print(solution())