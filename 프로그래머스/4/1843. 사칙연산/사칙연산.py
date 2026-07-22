def solution(arr):
    num_list = []
    op_list = []

    for i in range(len(arr)):
        if i % 2 == 0:
            num_list.append(int(arr[i]))
        else:
            op_list.append(arr[i])

    n = len(num_list)

    max_dp = [[-int(1e9)] * n for _ in range(n)]
    min_dp = [[int(1e9)] * n for _ in range(n)]

    for i in range(n):
        max_dp[i][i] = num_list[i]
        min_dp[i][i] = num_list[i]

    for length in range(2, n + 1):
        for start in range(n-length+1):
            end = start + length - 1

            for split in range(start, end):
                max_left = max_dp[start][split]
                min_left = min_dp[start][split]
                max_right = max_dp[split + 1][end]
                min_right = min_dp[split + 1][end]

                if op_list[split] == '+':
                    max_dp[start][end] = max(max_dp[start][end], max_left + max_right)
                    min_dp[start][end] = min(min_dp[start][end], min_left + min_right)
                else:
                    max_dp[start][end] =  max(max_dp[start][end],max_left - min_right)
                    min_dp[start][end] = min(min_dp[start][end],min_left - max_right)

    return max_dp[0][-1]