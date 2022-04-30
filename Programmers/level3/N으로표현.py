def solution(N, number):
    dp = [[]]
    for i in range(1, 9):
        temp = []
        temp.append(int(str(N) * i))
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    temp.append(k+l)
                    if k - l > 0:
                        temp.append(k-l)
                    temp.append(k*l)
                    if k != 0 and l != 0:
                        temp.append(k//l)
        if number in temp:
            return i
        dp.append(list(set(temp)))

    return -1