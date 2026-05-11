# 데이터 분석
# https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    for i in range(len(data)):
        if data[i][ext_dict[ext]] <= val_ext:
            answer.append(data[i])

    answer.sort(key=lambda x: x[ext_dict[sort_by]])

    return answer


data_ex = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext_ex = "date"
val_ext_ex = 20300501
sort_by_ex = 'remain'


print(solution(data_ex, ext_ex, val_ext_ex, sort_by_ex))
