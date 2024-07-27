# 햄버거 분배
# https://www.acmicpc.net/problem/19941





def solution():
    cnt = 0
    n, k = map(int, input().split())
    table = list(input())

    for i in range(n):
        if table[i] == 'P':             # 테이블에 사람이 앉아 있다면
            for j in range(-k, k+1):    # 앞, 뒤 테이블을 확인
                if j == 0:              # 본인의 자리는 패스
                    continue

                if i + j < 0 or i + j >= n:     # 테이블을 넘어가면 패스
                    continue

                if table[i+j] == 'H':           # 햄버거가 있다면
                    table[i+j] = 'X'            # 햄버거를 먹고
                    cnt += 1                    # 먹은 사람 1명 추가
                    break

    return cnt


print(solution())
