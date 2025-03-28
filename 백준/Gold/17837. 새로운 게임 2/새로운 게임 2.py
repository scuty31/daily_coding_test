def is_finish(n, board_piece):
    for x in range(n):
        for y in range(n):
            if len(board_piece[x][y]) >= 4:
                return True

    return False


def move(n, idx, board, piece_dict, board_piece):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    x, y, d = piece_dict[idx]
    nx, ny = x + dx[d], y + dy[d]

    # 체스판을 넘어가거나 파란색 칸일 경우 이동 방향을 반대로 바꾼다.
    if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 2:
        if d == 0:
            d = 1
        elif d == 1:
            d = 0
        elif d == 2:
            d = 3
        elif d == 3:
            d = 2

        nx, ny = x + dx[d], y + dy[d]

    # 이동하려는 칸이 체스판을 벗어나거나 파란색인 경우 가만히 있는다.
    if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 2:
        piece_dict[idx] = (x, y, d)
        return

    # 이동할 말 선택
    stack = board_piece[x][y]
    move_piece = stack[stack.index(idx):]
    for _ in range(len(move_piece)):
        board_piece[x][y].pop()

    # 이동하려는 칸이 흰색인 경우에는 가장 위에 말을 올려놓는다.
    if board[nx][ny] == 0:
        board_piece[nx][ny].extend(move_piece)

        for i in move_piece:
            px, py, pd = piece_dict[i]
            if i == idx:
                piece_dict[idx] = (nx, ny, d)
            else:
                piece_dict[i] = (nx, ny, pd)

    # 이동하려는 칸이 빨간색인 경우 이동하는 모든 말의 순서를 반대로 바꾼다.
    elif board[nx][ny] == 1:
        board_piece[nx][ny].extend(reversed(move_piece))

        for i in move_piece:
            px, py, pd = piece_dict[i]
            if i == idx:
                piece_dict[idx] = (nx, ny, d)
            else:
                piece_dict[i] = (nx, ny, pd)


def solution():
    n, k = map(int, input().split())
    board = list(list(map(int, input().split())) for _ in range(n))
    piece = list(list(map(int, input().split())) for _ in range(k))
    piece_dict = dict()
    board_piece = [[[] for _ in range(n)] for _ in range(n)]

    # 보드에 각 말들을 올려둠
    for i in range(k):
        x, y, d = piece[i]
        x -= 1
        y -= 1
        d -= 1

        piece_dict[i] = (x, y, d)
        board_piece[x][y].append(i)

    for i in range(1, 1001):
        for idx in range(k):
            move(n, idx, board, piece_dict, board_piece)

            if is_finish(n, board_piece):
                return i

    return -1


print(solution())