n = int(input())
# 숫자는 1부터, 리스트는 0부터 인식해서 임의적으로 1 증가시킴
dp = [0] * (n+1)
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])