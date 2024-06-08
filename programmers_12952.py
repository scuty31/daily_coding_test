# N-Queen


# 퀸을 놓았을 때
def put_queen(x, y, n, visited):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    visited[x][y] += 1

    for i in range(len(dx)):
        nx = x
        ny = y

        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                break

            visited[nx][ny] += 1


# 퀸을 제거했을 때
def delete_queen(x, y, n, visited):
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    visited[x][y] -= 1

    for i in range(len(dx)):
        nx = x
        ny = y

        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                break

            visited[nx][ny] -= 1


def queen(depth, n, visited, cnt):
    if depth >= n:
        cnt += 1

        return cnt

    for i in range(n):
        if visited[depth][i]:
            continue

        put_queen(depth, i, n, visited)             # 현재 자리에 퀸을 놓았을 때 다른 퀸을 놓을 수 없는 공간 표시
        cnt = queen(depth+1, n, visited, cnt)       # 다음 줄에 퀸을 놓기
        delete_queen(depth, i, n, visited)          # 퀸을 제거

    return cnt


def solution(n):
    answer = 0

    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        put_queen(0, i, n, visited)
        answer = queen(1, n, visited, answer)
        delete_queen(0, i, n, visited)

    return answer


print(solution(12))