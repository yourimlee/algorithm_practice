import sys

n, m = map(int, sys.stdin.readline().split())

li_1 = set()
li_2 = set()
for _ in range(n):
    li_1.add(sys.stdin.readline())
for _ in range(m):
    li_2.add(sys.stdin.readline())
    
res = sorted(list(li_1 & li_2))

print(len(res))

for i in res:
    print(i)