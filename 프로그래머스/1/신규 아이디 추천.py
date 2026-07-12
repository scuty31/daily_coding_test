def solution(new_id):
    answer = ''
    new_id = new_id.lower()     # 1단계 - 소문자 변환

    # 2단계 - 문자 제거
    new_id_list = []
    for alpha in new_id:
        if alpha.isalpha():
            new_id_list.append(alpha)
        elif alpha.isalnum():
            new_id_list.append(alpha)
        elif alpha == '-' or alpha == '_' or alpha == '.':
            new_id_list.append(alpha)

    new_id = ''.join(new_id_list)
    new_id_list.clear()

    # 3단계 - 마침표 2개 연속 제거
    for alpha in new_id:
        if len(new_id_list) == 0:
            new_id_list.append(alpha)
            continue
        if alpha == '.' and new_id_list[-1] == '.':
            continue
        new_id_list.append(alpha)

    # 4단계 - 마침표 위치 제거
    if len(new_id_list) > 0 and new_id_list[0] == '.':
        new_id_list.pop(0)
    if len(new_id_list) > 0 and new_id_list[-1] == '.':
        new_id_list.pop()

    # 5단계 - 빈 문자열 확인
    if len(new_id_list) == 0:
        new_id_list.append('a')

    # 6단계 - 길이 조절
    while len(new_id_list) >= 16:
        new_id_list.pop()

    if new_id_list[-1] == '.':
        new_id_list.pop()

    # 7단계 - 2자 이하인 경우
    if len(new_id_list) <= 2:
        while len(new_id_list) < 3:
            new_id_list.append(new_id_list[-1])

    answer = ''.join(new_id_list)

    return answer


new_id_input = "...!@BaT#*..y.abcdefghijklm"

print(solution(new_id_input))