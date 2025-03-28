def solution():
    n = int(input())
    triangle_list = []
    dp = []

    for i in range(n):
        triangle_list.append(list(map(int, input().split())))
        dp.append([0 for _ in range(len(triangle_list[i]))])

    dp[0][0] = triangle_list[0][0]
    
    if n == 1:
        return dp[0][0]
    
    dp[1][0] = triangle_list[1][0] + dp[0][0]
    dp[1][1] = triangle_list[1][1] + dp[0][0]

    for i in range(2, n):
        dp[i][0] = triangle_list[i][0] + dp[i-1][0]
        dp[i][-1] = triangle_list[i][-1] + dp[i-1][-1]

        for j in range(1, i):
            dp[i][j] = triangle_list[i][j] + max(dp[i-1][j-1], dp[i-1][j])

    return max(dp[n-1])


print(solution())