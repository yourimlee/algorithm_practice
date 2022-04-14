import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(1, n+1):
    com = combinations(num, i)
    for j in list(com):
        if sum(j) == s:
            cnt += 1

print(cnt)