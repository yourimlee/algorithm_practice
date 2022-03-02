n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

visited = [0] * (n+1)
res = []

def dfs(v):
    visited[v] = 1
    for i in range(1, n+1):
        if graph[v][i] == 1 and (i not in visited):
            res.append(i)
            dfs(i)
    return len(res)
    
print(dfs(1))