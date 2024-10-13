def solution():
	while True:
		password = input()
		is_acceptable = True

		if password == 'end':
			break

		if ('a' not in password and 'e' not in password and 'i' not in password and 'o' not in password and 'u' not in password):
			print(f'<{password}> is not acceptable.')
			continue

		c, v = 0, 0			# 자음, 모음
		last_word = ''

		for w in password:
			if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u':
				c = 0
				v += 1

			else:
				c += 1
				v = 0

			if c == 3 or v == 3:
				is_acceptable = False
				break

			if last_word != w:
				last_word = w

			elif last_word != 'o' and last_word != 'e':
				is_acceptable = False
				break

		if is_acceptable:
			print(f'<{password}> is acceptable.')
		else:
			print(f'<{password}> is not acceptable.')


solution()