def rule_1(s):
	s += 'A'

	return s


def rule_2(s):
	s += 'B'
	s = ''.join(list(reversed(list(s))))

	return s


def check_str(s, t):
	if s == t:
		return 1

	if len(s) == len(t):
		return 0

	answer_1 = check_str(rule_1(s), t)
	answer_2 = check_str(rule_2(s), t)

	if answer_1 == 1 or answer_2 == 1:
		print(1)
		exit()
	else:
		return 0


def solution():
	s = input()
	t = input()

	answer = check_str(s, t)
	print(answer)


solution()
