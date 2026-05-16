from collections import deque


def solution(players, m, k):
    server = deque()
    server_count = 0
    answer = 0

    for i in range(len(players)):
        # 사용을 마친 증설 서버 확인
        if len(server) > 0:
            if server[0][0] == i-k:
                _, cnt = server.popleft()
                server_count -= cnt

        # 증설 서버가 필요 없다면 넘기기
        if players[i] < m*(server_count+1):
            continue

        # 증설 서버 추가
        if players[i] >= m*server_count:
            add_server = (players[i] // m) - server_count       # 증설할 서버 개수
            answer += add_server                                # 증설한 서버 count 하기
            server.append((i, add_server))                      # 언제 몇개를 증설했는지 기록
            server_count += add_server                          # 총 증설한 서버 개수수

    return answer


player_input = [0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0]
m_input = 5
k_input = 1

print(solution(player_input, m_input, k_input))