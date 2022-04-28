import sys
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v):
    visited[v] = 1
    for i in range(1, n+1):
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)

visited = [0] * (n+1); cnt = 0
for i in range(1, n+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)