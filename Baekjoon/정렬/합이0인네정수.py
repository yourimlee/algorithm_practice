n = int(input())
alist, blist, clist, dlist = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    alist.append(a); blist.append(b)
    clist.append(c); dlist.append(d)

test = {}
res = 0
for i in range(n):
    for j in range(n):
        ab = alist[i] + blist[j]
        if ab in test:
            test[ab] += 1
        else:
            test[ab] = 1

for i in range(n):
    for j in range(n):
        cd = -(clist[i] + dlist[j])
        if cd in test:
            res += test[cd]

print(res)