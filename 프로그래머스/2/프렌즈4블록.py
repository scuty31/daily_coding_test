def remove_square(board, square):
    for x, y in square:
        board[x][y] = '.'


def set_board(m, n, board):
    for y in range(n):
        empty_board_x = m-1

        for x in reversed(range(m)):
            if board[x][y] != '.':
                board[empty_board_x][y] = board[x][y]
                empty_board_x -= 1

        for x in range(empty_board_x+1):
            board[x][y] = '.'


def solution(m, n, board):
    answer = 0

    # board 나누기
    for i in range(m):
        board[i] = list(board[i])

    while True:
        square = set()

        # 네모 찾기
        for x in range(m-1):
            for y in range(n-1):
                board_block = board[x][y]
                if board_block == '.':
                    continue

                if board_block == board[x+1][y] == board[x][y+1] == board[x+1][y+1]:
                    square.add((x, y))
                    square.add((x+1, y))
                    square.add((x, y+1))
                    square.add((x+1, y+1))

        # 네모가 없으면 끝
        if len(square) == 0:
            break

        # 네모 제거
        answer += len(square)
        remove_square(board, square)

        # board 정렬
        set_board(m, n, board)

    return answer


m_input = 6
n_input = 6
board_input = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m_input, n_input, board_input))