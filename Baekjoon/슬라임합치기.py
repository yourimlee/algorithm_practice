n = int(input())
num = list(map(int, input().split()))

num.sort(reverse=True)
res = 0
tot = 0

for i in range(0, n-1):
    res = num[i] * num[i+1]
    num[i+1] = num[i] + num[i+1]
    tot += res
    
print(tot)