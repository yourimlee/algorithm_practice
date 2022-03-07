n = int(input())
oil = list(map(int, input().split()))
cost = list(map(int, input().split()))

price = 0
m = cost[0]
for i in range(n-1):
    if cost[i] < m:
        m = cost[i]
    price += m * oil[i]
    
print(price)