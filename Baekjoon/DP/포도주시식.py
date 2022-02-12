n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))
dp = [0 for _ in range(n)]

if n == 1:
    dp[0] = wine[0]
elif n == 2:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])
    
    for i in range(3, n):
        dp[i] = max(dp[i-1], max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i]))
    
    print(dp[n-1])