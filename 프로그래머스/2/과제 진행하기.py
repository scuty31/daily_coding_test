def solution(plans):
    for i in range(len(plans)):
        hour = int(plans[i][1][:2])
        minute = int(plans[i][1][3:])

        time_hm = hour*60 + minute
        left_time = int(plans[i][2])

        plans[i][1] = time_hm
        plans[i][2] = left_time

    plans.sort(key=lambda x:x[1])

    answer = []
    now_task = [plans[0]]
    now_time = plans[0][1]

    for task_name, task_start_time, task_left_time in plans[1:]:




    return answer


input_a = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
print(solution(input_a))