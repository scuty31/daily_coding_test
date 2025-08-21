def solution(dartResult):
    answer = 0
    reward = [0, 0, 0]

    idx = 0
    dart_list = list(dartResult)

    for i in range(len(dart_list)):
        n = dart_list[i]

        # S, D, T 에서 이미 처리함.
        if n == '#' or n == '*':
            continue

        if n == 'S' or n == 'D' or n == 'T':
            # Double일 경우 2제곱
            if n == 'D':
                reward[idx] **= 2

            # Triple일 경우 3제곱
            elif n == 'T':
                reward[idx] **= 3

            if i + 1 < len(dart_list):
                # 스타상이면 현재 점수와 이전 점수 2배
                if dart_list[i + 1] == '*':
                    reward[idx] *= 2

                    if idx > 0:
                        reward[idx - 1] *= 2

                # 아차상이면 해당 점수는 마이너스
                elif dart_list[i + 1] == '#':
                    reward[idx] *= (-1)

            # 다음 기회로 넘어감
            idx += 1

            continue

        if n == '1' and dart_list[i+1] == '0':
            n = 10

        if n == '0':
            continue

        reward[idx] = int(n)

    # 전체 점수를 더함
    for i in range(3):
        answer += reward[i]

    return answer