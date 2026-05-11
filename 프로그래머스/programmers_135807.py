# 숫자 카드 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/135807

def gcd(n, m):
    while m > 0:
        n, m = m, n % m

    return n


def solution(arrayA, arrayB):
    answer = 0

    arrayA.sort()
    arrayB.sort()
    a_gcd = arrayA[0]
    b_gcd = arrayB[0]
    a_bool = True
    b_bool = True

    for i in range(1, len(arrayA)):
        if arrayA[i] % a_gcd != 0:
            a_bool = False
            break

    for j in range(1, len(arrayB)):
        if arrayB[j] % b_gcd != 0:
            b_bool = False
            break

    if not a_bool:
        a_gcd = gcd(arrayA[0], arrayA[1])

        for i in range(2, len(arrayA)):
            a_gcd = gcd(a_gcd, arrayA[i])

    if not b_bool:
        b_gcd = gcd(arrayB[0], arrayB[1])

        for j in range(2, len(arrayB)):
            b_gcd = gcd(b_gcd, arrayB[j])

    a_bool = True
    b_bool = True

    for a in arrayA:
        if a % b_gcd == 0:
            a_bool = False
            break

    if a_bool:
        answer = max(answer, b_gcd)

    num_bool = True
    for b in arrayB:
        if b % a_gcd == 0:
            b_bool = False
            break

    if b_bool:
        answer = max(answer, a_gcd)

    return answer


array_a = [14, 35, 119]
array_b = [18, 30, 102]

print(solution(array_a, array_b))