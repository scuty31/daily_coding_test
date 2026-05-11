def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_list(nums):
    answer = nums[0]

    for num in nums[1:]:
        answer = lcm(answer, num)

    return answer


def solution(signals):
    t = 1
    cycles = []

    for i in range(len(signals)):
        cycles.append(sum(signals[i]))

    limit = lcm_list(cycles)

    while True:
        is_yellow = True

        for G, Y, R in signals:
            cycle = G + Y + R
            pos = (t-1) % cycle

            if not (G <= pos < G+Y):
                is_yellow = False
                break

        if is_yellow:
            break

        if t > limit:
            t = -1
            break

        t += 1

    return t