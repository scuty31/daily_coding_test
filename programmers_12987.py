def solution(A, B):
	A.sort()
	B.sort()

	if min(A) >= max(B):
		return 0

	idx = 0
	while B:
		if A[idx] < B[0]:
			idx += 1

		B.pop(0)

	answer = idx

	return answer


a = [5,1,3,7]
b = [2,2,6,8]

print(solution(a, b))