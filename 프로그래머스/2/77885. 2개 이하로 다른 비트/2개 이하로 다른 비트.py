def change_bit(n):
    bit_num = []

    while n:
        bit_num.append(n % 2)
        n //= 2

    if bit_num.count(0) == 0:
        bit_num.append(0)

    return bit_num


def change_dec(bit_n):
    num = 0

    for i in range(len(bit_n)):
        num += bit_n[i] * (2**i)

    return num


def solution(numbers):
    answer = []

    for n in numbers:
        bit_n = change_bit(n)

        if n % 2 == 1:
            for i in range(len(bit_n)):
                if bit_n[i] == 0:
                    bit_n[i] = 1
                    bit_n[i-1] = 0
                    break

        else:
            for i in range(len(bit_n)):
                if bit_n[i] == 0:
                    bit_n[i] = 1
                    break

        answer.append(change_dec(bit_n))

    return answer