def solution(names):
	answer = []
	for i in range(0,len(names),5):
		answer.append(names[i])

	return answer


names_input = ["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]

print(solution(names_input))