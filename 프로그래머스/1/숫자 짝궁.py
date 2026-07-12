def solution(X, Y):
    answer = ''

    X_list = list(map(int, list(X)))
    Y_list = list(map(int, list(Y)))
    X_set = list(set(X_list))
    Y_set = list(set(Y_list))
    common_dict = dict()
    common_list = []

    # 공통된 숫자 찾기
    for idx in range(10):
        if idx in X_set and idx in Y_set:
            common_list.append(idx)

    # 공통된 숫자가 없다면 -1 return
    if len(common_list) == 0:
        return '-1'

    # 공통된 숫자가 0만 있다면 0 return
    if len(common_list) == 1 and common_list[0] == 0:
        return '0'

    # 공통된 숫자의 count 세기
    for i in range(len(common_list)):
        num = common_list[i]
        x_count = X_list.count(num)
        y_count = Y_list.count(num)
        common_dict[num] = min(x_count, y_count)

    for key, value in reversed(common_dict.items()):
        add_str = str(key)*value
        answer += add_str

    return answer


X_input = '00481264123987123'
Y_input = "1230012698124098123"

print(solution(X_input, Y_input))