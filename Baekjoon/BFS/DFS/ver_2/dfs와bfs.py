from collections import deque

def dfs(v, visited=[]):
    visited.append(v)
    print(v, end =' ')
    for i in range(1, n+1):
        if graph[v][i] == 1 and (i not in visited):
            dfs(i, visited)
            
def bfs(v):
    visited = [v]
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if graph[v][i] == 1 and (i not in visited):
                visited.append(i)
                queue.append(i)

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1
    
dfs(v)
print()
bfs(v)