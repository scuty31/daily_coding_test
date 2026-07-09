from collections import deque


def check_line(sx, sy, ex, ey):
    route = [(sx, sy)]

    while sx != ex:
        if sx < ex:
            sx += 1
        else:
            sx -= 1
        route.append((sx, sy))

    while sy != ey:
        if sy < ey:
            sy += 1
        else:
            sy -= 1
        route.append((sx, sy))

    return route


def solution(points, routes):
    answer = 0
    lines = []

    for route in routes:
        total_line = []

        for j in range(len(route) - 1):
            s = route[j] - 1
            e = route[j + 1] - 1

            sx, sy = points[s]
            ex, ey = points[e]

            line = check_line(sx, sy, ex, ey)

            if j == 0:
                total_line += line
            else:
                total_line += line[1:]

        lines.append(total_line)

    idx = 0
    limit = 0

    for i in range(len(lines)):
        limit = max(limit, len(lines[i]))

    while idx < limit:
        now_robots = dict()

        for i in range(len(lines)):
            if idx >= len(lines[i]):
                continue

            if now_robots.get(lines[i][idx]):
                if now_robots[lines[i][idx]] == 1:
                    answer += 1
                    now_robots[lines[i][idx]] += 1
            else:
                now_robots[lines[i][idx]] = 1

        idx += 1

    return answer


points_input = [[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]]
routes_input = [[2, 3, 4, 5], [1, 3, 4, 5]]

print(solution(points_input, routes_input))