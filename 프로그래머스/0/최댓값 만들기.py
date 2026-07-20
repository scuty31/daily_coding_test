def solution(numbers):
	numbers.sort()
	answer = max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])

	return answer


numbers_input = [0, -31, 24, 10, 1, 9]
print(solution(numbers_input))