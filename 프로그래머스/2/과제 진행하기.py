def solution(plans):
    for i in range(len(plans)):
        hour = int(plans[i][1][:2])
        minute = int(plans[i][1][3:])

        time_hm = hour*60 + minute
        finish_time = int(plans[i][2])

        plans[i][1] = time_hm
        plans[i][2] = finish_time

    plans.sort(key=lambda x:x[1])

    answer = []
    work_list = []
    now_time = 0

    for i in range(len(plans)):
        now_time = plans[i][1]

        if work_list:
            stop_work, stop_time, left_time = work_list.pop()
            running_time = now_time - stop_time

            while running_time:
                if running_time < left_time:
                    work_list.append((stop_work, now_time, left_time-running_time))
                    running_time = 0

                elif running_time == left_time:
                    answer.append(stop_work)
                    running_time = 0

                else:
                    running_time -= left_time
                    answer.append(stop_work)
                    if work_list:
                        stop_work, stop_time, left_time = work_list.pop()
                    else:
                        running_time = 0

        work_list.append((plans[i][0], plans[i][1], plans[i][2]))

    for work, _, _ in reversed(work_list):
        answer.append(work)

    return answer


plans_input = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
print(solution(plans_input))