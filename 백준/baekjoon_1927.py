import heapq
import sys


def solution():
	n = int(sys.stdin.readline().strip())
	queue = []

	for _ in range(n):
		num = int(sys.stdin.readline().strip())

		if num == 0:
			if len(queue):
				print(heapq.heappop(queue))
			else:
				print(0)
		else:
			heapq.heappush(queue, num)


solution()