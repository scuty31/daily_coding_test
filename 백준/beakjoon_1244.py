
def switch_on_off(n, switch, person):
	sex, num = person

	# 남자인 경우
	if sex == 1:
		idx = num

		while idx <= n:
			if switch[idx]:
				switch[idx] = 0
			else:
				switch[idx] = 1

			idx += num

	# 여자인 경우
	else:
		i, j = num-1, num+1

		if switch[num]:
			switch[num] = 0
		else:
			switch[num] = 1

		if i <= 0 or j > n:
			return

		while switch[i] == switch[j]:
			if switch[i]:
				switch[i] = 0
				switch[j] = 0

			else:
				switch[i] = 1
				switch[j] = 1

			i -= 1
			j += 1

			if i <= 0 or j > n:
				break


def solution():
	n = int(input())
	switch = [-1] + list(map(int, input().split()))
	people_num = int(input())
	people = list()

	for _ in range(people_num):
		sex, num = map(int, input().split())
		people.append((sex, num))

	for i in range(people_num):
		switch_on_off(n, switch, people[i])

	cnt = 0
	for j in range(1, len(switch)):
		print(switch[j], end=' ')
		cnt += 1

		if cnt == 20:
			print()
			cnt = 0


solution()