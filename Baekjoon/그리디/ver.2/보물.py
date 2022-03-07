n = int(input())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
alist.sort()
blist.sort(reverse = True)

res = 0
for i in range(n):
    res += alist[i] * blist[i]

print(res)