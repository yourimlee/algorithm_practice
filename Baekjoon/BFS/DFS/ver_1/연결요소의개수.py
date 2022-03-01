import sys
sys.setrecursionlimit(10000)
from collections import deque

n, m = map(int, input().split())
link = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    link[x].append(y)
    link[y].append(x)
cnt = 0

def dfs(v):
    visited[v] = 1
    for i in link[v]:
        if visited[i] == 0:
            dfs(i)
            
for j in range(1, n+1):
    if visited[j] == 0:
        dfs(j)
        cnt += 1
        
print(cnt)