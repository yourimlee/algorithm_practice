import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
sum_value = 0
sum_d = [0]

for y in num:
    sum_value += y
    sum_d.append(sum_value)

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(sum_d[e] - sum_d[s-1])