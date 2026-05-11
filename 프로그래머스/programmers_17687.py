def change(n, num):
	num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
	result = []
	if num == 0:
		return '0'

	while num:
		result.append(num_list[num % n])
		num //= n

	return ''.join(list(reversed(result)))


def solution(n, t, m, p):
	answer = ''
	result = ''
	p -= 1

	idx = 0
	while True:
		result += change(n, idx)
		idx += 1

		if len(result) >= (t * m) + p:
			break

	for i in range(p, t*m, m):
		answer += result[i]

	return answer


nn = 16
tt = 16
mm = 2
pp = 1

print(solution(nn, tt, mm, pp))
