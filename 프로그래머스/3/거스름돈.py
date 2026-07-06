def solution(n, money):
    money.sort()
    dp = [0 for _ in range(n+1)]
    dp[0] = 1

    for coin in money:
        for amount in range(coin, n+1):
            dp[amount] += dp[amount - coin]

    answer = dp[-1]

    return answer % 1000000007


n_input = 5
money_input = [1, 2, 5]

print(solution(n_input, money_input))