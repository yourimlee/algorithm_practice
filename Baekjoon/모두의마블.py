n = int(input())
c = list(map(int, input().split()))
c.sort(reverse=True)
result = 0

for i in range(len(c)):
    if i <= 1:
        result += c[i]
    else:
        result += c[0]+c[i]

print(result)