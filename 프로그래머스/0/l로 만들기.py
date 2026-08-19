def solution(myString):
	answer = ''
	targets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
	for target in targets:
		myString = myString.replace(target, 'l')
	return myString


myString_input = "abcdevwxyz"
print(solution(myString_input))