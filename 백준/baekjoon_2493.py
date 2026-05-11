def solution():
	n = int(input())
	top_list = list(map(int, input().split()))
	answer = [0] * n

	stack = []
	while top_list:
		top = top_list.pop()		# 기준 탑의 높이
		idx = len(top_list)			# 기준 탑의 위치

		# 비교할 탑이 없다면 탑 추가하고 넘어가기
		if len(stack) == 0:
			stack.append((top, idx))
			continue

		# 오른쪽에 위치한 탑이 기준 탑보다 작아서 탑에 전파가 닿았을 때
		if stack[-1][0] < top:
			for _ in range(len(stack)):
				top_tmp, idx_tmp = stack.pop()

				# 비교할 탑이 기준 탑보다 높이가 작으면 answer에 기록
				if top > top_tmp:
					answer[idx_tmp] = idx + 1

				# 높이가 더 크면 그 이후의 탑들 역시 다 크기 때문에 반복문 빠져나오기
				else:
					stack.append((top_tmp, idx_tmp))
					break

		# 기준 탑을 비교할 탑들에 추가
		stack.append((top, idx))

	return ' '.join(list(map(str, answer)))


print(solution())