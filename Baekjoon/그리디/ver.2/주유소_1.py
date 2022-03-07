n = int(input())
oil = list(map(int, input().split()))
cost = list(map(int, input().split()))

price = 0
if cost.count('1') == n:
    price += sum(oil)
    
if cost[0] == min(cost):
    price += sum(oil) * cost[0]
else:
    for i in range(1, n-1):
        price += oil[0] * cost[0]
        if cost[i] < cost[i-1]:
            price += oil[i] * cost[i]
        else:
            price += oil[i] * cost[i-1]
    
print(price)