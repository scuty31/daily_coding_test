def solution(s):
    answer = ''
    s_list = list(s)
    idx = 0

    for i in range(len(s_list)):
        if s_list[i] == '' or s_list[i] == ' ':
            idx = 0
            continue

        if idx % 2 == 0:
            s_list[i] = s_list[i].upper()
        else:
            s_list[i] = s_list[i].lower()

        idx += 1

    answer = ''.join(s_list)

    return answer