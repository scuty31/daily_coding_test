# 2. 향료 추가
def add_perfume(N, S, v):
	S[N+1] = v
	return N+1


# 3. 향료 폐기
def delete_perfume(N, S, idx):
	S[idx] = 0


def solution():
	Q = int(input())

	perfume_list = list(map(int, input().split()))
	N = perfume_list[1]
	Q -= 1

	# 1. 향료 준비
	S = dict()
	for i in range(2, len(perfume_list)):
		S[i] = perfume_list[i]

	dp = []



#solution()

s = "hello"

for o in s:
	print(o)