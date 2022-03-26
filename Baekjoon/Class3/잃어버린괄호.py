cal = input().split('-')
res = 0
for i in cal[0].split('+'):
    res += int(i)
for i in cal[1:]:
    for j in i.split('+'):
        res -= int(j)

print(res)