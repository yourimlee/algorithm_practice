n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    m1, m2 = map(int, input().split())
    graph[m1].append(m2)
    graph[m2].append(m1)
visited = [0] * (n+1)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            
cnt = 0
for i in range(1, n+1):
    if visited[i] == 0:
       dfs(i)
       cnt += 1
       
print(cnt) 