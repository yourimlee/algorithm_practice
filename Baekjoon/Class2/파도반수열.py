t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * (n+1)
    if n == 1:
        dp[1] = 1
    elif n == 2:
        dp[1], dp[2] = 1, 1
    elif n == 3:
        dp[1], dp[2], dp[3] = 1, 1, 1
    else:
        dp[1], dp[2], dp[3] = 1, 1, 1
        for i in range(4, n+1):
            dp[i] = dp[i-3] + dp[i-2]

    print(dp[n])