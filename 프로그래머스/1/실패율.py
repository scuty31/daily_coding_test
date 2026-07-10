def solution(N, stages):
    answer = []

    players = {i: 0 for i in range(N + 1)}

    for level in stages:
        for i in range(level):
            players[i] += 1

    pre_players_cnt = 0
    fail = [(0, i) for i in range(N + 1)]

    for level in range(1, N + 1):
        all_player = len(stages) - pre_players_cnt
        fail_player = all_player - players[level]
        fail[level] = (fail_player / all_player, level)

        pre_players_cnt += fail_player

    fail.pop(0)
    fail.sort(key=lambda x: x[0], reverse=True)

    for _, stage in fail:
        answer.append(stage)

    return answer


N_input = 5
stages_input = 	[2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N_input, stages_input))