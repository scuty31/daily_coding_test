def solution(N, number):
    answer = -1

    if N == number:
        return 1

    # 각 개수를 사용해 만들 수 있는 숫자들
    dp = [set() for _ in range(9)]
    dp[1].add(N)

    for i in range(2, len(dp)):
        dp[i].add(int(str(N)*i))

        for j in range(1, i):
            for n in dp[j]:
                for m in dp[i-j]:
                    if n + m >= 0:
                        dp[i].add(n + m)
                    if n - m >= 0:
                        dp[i].add(n - m)
                    if m - n >= 0:
                        dp[i].add(m - n)
                    dp[i].add(n*m)
                    if m != 0:
                        dp[i].add((-n)//(-m))
                    if n != 0:
                        dp[i].add((-m)//(-n))

        if number in dp[i]:
            answer = i
            break

    return answer