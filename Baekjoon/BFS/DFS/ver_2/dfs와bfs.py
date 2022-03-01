import sys
from collections import deque

def dfs(v):
    print(v, end ='')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
def bfs(v):
    visited[v] = True
    queue = deque([n])
    while queue:
        l = queue.popleft()
        print(l, end='')
        for i in graph[l]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1
visited = [False] * (n+1)

dfs(v)
visited = [False] * (n+1)
print()
bfs(v)