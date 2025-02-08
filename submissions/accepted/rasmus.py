
n = int(input())
cost = [int(i) for i in input().split()]
if n == 1:
    print(cost[0])
else:
    dp = [0] * n
    dp[0], dp[1] = cost[0], cost[0] + cost[1]

    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    print(dp[-1])