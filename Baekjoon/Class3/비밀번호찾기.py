import sys

n, m = map(int, sys.stdin.readline().split())
keyword = {}
for _ in range(n):
    a, b = sys.stdin.readline().split()
    keyword[a] = b

for _ in range(m):
    print(keyword[sys.stdin.readline().rstrip()])