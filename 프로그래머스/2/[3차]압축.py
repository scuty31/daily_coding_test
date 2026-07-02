from collections import deque


def solution(msg):
    answer = []
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    doc = dict()

    for i in range(1, 27):
        doc[alpha[i-1]] = i

    msg_queue = deque(msg)

    while msg_queue:
        w = msg_queue.popleft()

        if len(msg_queue) <= 0:
            answer.append(doc[w])
            break

        c = msg_queue.popleft()

        # 현재 입력과 일치하는 가장 긴 문자열 w 찾기
        while doc.get(w+c):
            w = w+c
            if len(msg_queue) > 0:
                c = msg_queue.popleft()
            else:
                c = ''
                break

        answer.append(doc[w])
        doc[w+c] = len(doc)+1

        if c == '':
            break
        msg_queue.appendleft(c)

    return answer

msg_input = 'ABABABABABABABAB'

print(solution(msg_input))