def clock(schedules):
    for i in range(len(schedules)):
        schedules[i] += 10
        if schedules[i] % 100 >= 60:
            schedules[i] += 40
            

def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    clock(schedules)

    for i in range(n):
        day = startday - 1
        get_present = True

        for j in range(len(timelogs[i])):
            day += 1
            if day % 7 == 6 or day % 7 == 0:
                continue

            if timelogs[i][j] > schedules[i]:
                get_present = False
                break

        if get_present:
            answer += 1

    return answer