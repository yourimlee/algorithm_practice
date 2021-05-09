def solution(n, money):
    # 행은 현재 가지고 있는 동전, 열은 지불하고자 하는 금액
    dp = [[0]*(n+1) for _ in range(len(money))]
    dp[0][0] = 1

    for i in range(money[0], n+1, money[0]):
        dp[0][i] = 1
    for y in range(1, len(money)):
        for x in range(n+1):
            if x >= money[y]:
                dp[y][x] = (dp[y-1][x] + dp[y][x-money[y]]) %1000000007
            else:
                dp[y][x] = dp[y-1][x]
    return dp[-1][-1]

