from collections import deque


def check_str(s, t):
	queue = deque()
	visited = []
	queue.append(t)
	visited.append(t)

	while queue:
		t = queue.popleft()

		if t == s:
			return 1

		if len(t) < len(s):
			continue

		if t[-1] == 'A':
			t1 = t[:-1]
			if t1 not in visited:
				queue.append(t1)

		if t[0] == 'B':
			t2 = list(reversed(t[1:]))
			if t2 not in visited:
				queue.append(t2)

	return 0


def solution():
	s = list(input())
	t = list(input())

	answer = check_str(s, t)

	return answer


print(solution())
