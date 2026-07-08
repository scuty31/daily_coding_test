from collections import deque


def set_shape(shape):
    min_x = min(x for x, y in shape)
    min_y = min(y for x, y in shape)

    norm = sorted([(x - min_x, y - min_y) for x, y in shape])

    return norm


def get_shape(x, y, table, visited, n, m):
    queue = deque()
    shape = []

    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        shape.append((x, y))

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if table[nx][ny] == 0:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))

    shape = set_shape(shape)

    return shape


def get_hole(x, y, game_board, visited, n, m):
    queue = deque()
    shape = []

    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        shape.append((x, y))

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if game_board[nx][ny] == 1:
                continue
            if visited[nx][ny]:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))

    shape = set_shape(shape)

    return shape


def turn_piece(piece):
    turned_piece = []
    for x, y in piece:
        turned_piece.append((y, -x))

    shape = set_shape(turned_piece)

    return shape



def solution(game_board, table):
    answer = 0
    n = len(game_board)
    m = len(game_board[0])
    table_visited = [[False] * m for _ in range(n)]
    board_visited = [[False] * m for _ in range(n)]
    pieces = []
    holes = []

    for x in range(n):
        for y in range(m):
            if table[x][y] == 1 and not table_visited[x][y]:
                pieces.append(get_shape(x, y, table, table_visited, n, m))
            if game_board[x][y] == 0 and not board_visited[x][y]:
                holes.append(get_hole(x, y, game_board, board_visited, n, m))

    for piece in pieces:
        if piece in holes:
            answer += len(piece)
            holes.pop(holes.index(piece))
        else:
            turned_piece = piece
            for _ in range(3):
                turned_piece = turn_piece(turned_piece)

                if turned_piece in holes:
                    answer += len(turned_piece)
                    holes.pop(holes.index(turned_piece))
                    break

    return answer


game_board_input = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table_input = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

print(solution(game_board_input, table_input))