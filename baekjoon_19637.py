def b_search(combat_power, power, s, e):
	mid = (s + e) // 2

	if combat_power[mid-1] < power <= combat_power[mid]:
		return mid
	elif combat_power[mid] < power:
		return b_search(combat_power, power, mid+1, e)
	else:
		return b_search(combat_power, power, s, mid-1)


def solution():
	n, m = map(int, input().split())
	combat_power_dict = dict()
	combat_power = []

	for _ in range(n):
		power, power_num = input().split()
		if int(power_num) not in combat_power:
			combat_power.append(int(power_num))
			combat_power_dict[len(combat_power)] = power

	combat_power.insert(0, 0)

	for _ in range(m):
		player_power = int(input())
		if player_power == 0:
			target = 1
		else:
			target = b_search(combat_power, player_power, 0, n)

		print(combat_power_dict[target])


solution()