expression = input().split('-')

res = 0
for i in expression[0].split('+'):
    res += int(i)
for j in expression[1:]:
    for k in j.split('+'):
        res -= int(k)
print(res)