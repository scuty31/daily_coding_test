from collections import deque


def solution():
	n = int(input())
	cards = deque()

	for i in range(1, n+1):
		cards.append(i)

	while True:
		if len(cards) == 1:
			break

		cards.popleft()
		cards.append(cards.popleft())

	return cards[0]

print(solution())