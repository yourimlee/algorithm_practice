n = int(input())
time, money = [], []
for _ in range(n):
    t, m = map(int, input().split())
    time.append(t); money.append(m)

dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if (i + time[i]) > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], money[i] + dp[i + time[i]])

print(dp[0])
