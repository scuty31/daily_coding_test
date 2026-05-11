import math

def solution(signals):
    t = 1
    cycles = []

    for i in range(len(signals)):
        cycles.append(sum(signals[i]))

    limit = math.lcm(*cycles)

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


print(solution([[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]]))