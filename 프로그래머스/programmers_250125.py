# 이웃한 칸
# https://school.programmers.co.kr/learn/courses/30/lessons/250125


def solution(board, h, w):
    n = len(board)
    count = 0

    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]

        if h_check < 0 or w_check < 0 or h_check >= n or w_check >= n:
            continue

        if board[h][w] == board[h_check][w_check]:
            count += 1

    return count


board_ex = [["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]]
h_ex = 0
w_ex = 1

print(solution(board_ex, h_ex, w_ex))