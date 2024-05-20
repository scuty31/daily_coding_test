# 오픈채팅방
# https://school.programmers.co.kr/learn/courses/30/lessons/42888

"""
오픈 채팅방에는 본래 닉네임이 나닌 가상의 닉네임을 사용하여 채팅방에 들어갈 수 있다.
김크루는 사람들이 들어오고, 나가는 것을 볼 수 있는 관리자 창을 만들려고 한다.

채팅방에 누군가가 들어오면 다음 메시지가 출력된다.
'[닉네임]님이 들어왔습니다.'

채팅방에 누군가가 나가면 다음 메시지가 출력된다.
'[닉네임]님이 나갔습니다.'

채팅방에서 닉네임을 변경하는 방법은 다음과 같이 주어진다.
- 채팅방을 나간 후, 새로운 닉네임으로 다시 들어온다.
- 채팅방에서 닉네임을 변경한다.

닉네임을 변경했다면 기존 닉네임이 변경된다.

채팅방은 중복 닉네임을 허용한다.

채팅방과 관련된 모든 기록이 매개변수로 주어질 때,
모든 기록이 처리된 후, 최종적으로 관리자가 보는 메시지를 구하여라.
"""

"""
딕셔너리를 이용하여 유저 아이디 별로 닉네임을 저장한다.
이후, Enter와 Leave에 맞게 메시지를 출력한다.
"""


def solution(record):
    nickname_dict = dict()
    answer = []

    # 유저가
    for i in range(len(record)):
        tmp_list = list(record[i].split())

        # record 나누기
        op = tmp_list[0]
        user_id = tmp_list[1]
        nickname = ''

        # 만약 유저가 들어왔거나 닉네임을 변경하면 닉네임 변경
        if len(tmp_list) == 3:
            nickname = tmp_list[2]

        if op != 'Leave':
            nickname_dict[user_id] = nickname

    for i in range(len(record)):
        tmp_list = list(record[i].split())

        op = tmp_list[0]
        user_id = tmp_list[1]

        if op == 'Enter':
            answer.append(nickname_dict[user_id] + "님이 들어왔습니다.")
        elif op == 'Leave':
            answer.append(nickname_dict[user_id] + "님이 나갔습니다.")

    return answer


record_ex = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record_ex))
