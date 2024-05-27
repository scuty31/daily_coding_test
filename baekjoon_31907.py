# GIST 찍기
# https://www.acmicpc.net/problem/31907

"""
다음과 같은 그림이 있다.

G...
.I.T
..S.

해당 그림을 K배 확대한 그림을 출력하여라.
"""

"""
(K*4) * (K*3) 크기의 배열을 선언한다.
해당 배열에 GIST를 각각 추가한다.
"""

def solution():
    k = int(input())
    answer = [['.' for _ in range(k*4)] for _ in range(k*3)]
    x = 0
    y = 0

    for i in range(k):
        for j in range(k):
            answer[x+i][y+j] = 'G'

    x += k
    y += k

    for i in range(k):
        for j in range(k):
            answer[x+i][y+j] = 'I'

    x += k
    y += k

    for i in range(k):
        for j in range(k):
            answer[x+i][y+j] = 'S'

    x -= k
    y += k

    for i in range(k):
        for j in range(k):
            answer[x+i][y+j] = 'T'

    return answer


result = solution()

for idx in range(len(result)):
    for jdx in range(len(result[0])):
        print(result[idx][jdx], end='')
    print()