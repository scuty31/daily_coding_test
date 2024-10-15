def solution():
	n = int(input())
	word_list = list()
	s_word = list(input())

	for _ in range(n-1):
		word_list.append(list(input()))

	s_word.sort()
	answer = 0

	for i in range(len(word_list)):
		check_word = sorted(word_list[i])

		if len(s_word) - 1 == len(check_word):		# 문자 하나를 뺀 경우
			for j in range(len(s_word)):
				if s_word[j] in check_word:
					check_word.pop(check_word.index(s_word[j]))

			if len(check_word) == 0:
				answer += 1

		elif len(s_word) + 1 == len(check_word):		# 문자 하나를 더한 경우
			for j in range(len(s_word)):
				if s_word[j] in check_word:
					check_word.pop(check_word.index(s_word[j]))

			if len(check_word) == 1:
				answer += 1

		elif len(s_word) == len(check_word):			# 문자 하나를 변경 하거나 순서를 변경한 경우
			if s_word == check_word:
				answer += 1
			else:
				for j in range(len(s_word)):
					if s_word[j] in check_word:
						check_word.pop(check_word.index(s_word[j]))

				if len(check_word) == 1:
					answer += 1

	return answer


print(solution())
