num = list(map(int, input().split()))
check = []

for i in range(len(num)):
    check.append(num[i] * num[i])
    
print(sum(check)%10)