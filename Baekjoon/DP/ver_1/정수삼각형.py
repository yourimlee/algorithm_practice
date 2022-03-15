import sys
input = sys.stdin.readline

n = int(input())
num = []
for _ in range(n):
    num.append(list(map(int, input().split())))

if n == 1:
    print(num[0][0])
else:
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                num[i][0] += num[i-1][0]
            if j == i:
                num[i][j] += num[i-1][-1]
            else:
                num[i][j] += max(num[i-1][j], num[i-1][j-1])
            
    print(max(num[-1]))
            