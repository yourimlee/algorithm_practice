from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(v, visited = []):
    visited.append(v)
    print(v, end = ' ')
    for i in range(n+1):
        if graph[v][i] == 1 and i not in visited:
            dfs(i, visited)

def bfs(v):
    visited = [v]
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in range(n+1):
            if graph[v][i] == 1 and i not in visited:
                visited.append(i)
                q.append(i)

dfs(v)
print()
bfs(v)