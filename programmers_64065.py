# 튜플


def solution(s):
    answer = []
    s = s.replace('{', '', 1)
    s_list = s.split('{')
    s_list.pop(0)

    for i in range(len(s_list)):
        s_list[i] = s_list[i].replace('{', "").replace('}', "")
        s_list[i] = s_list[i].split(',')

        for j in range(len(s_list[i])):
            if s_list[i][j] == '':
                s_list[i].pop(j)
            else:
                s_list[i][j] = int(s_list[i][j])

    s_list.sort(key=len)

    for i in range(len(s_list)):
        for j in s_list[i]:
            if j not in answer:
                answer.append(j)
                break

    return answer


s_ex = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s_ex))