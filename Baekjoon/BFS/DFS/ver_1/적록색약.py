from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
                
visited = [[0] * n for _ in range(n)]
cnt_normal = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt_normal += 1
            
## 적록색맹인 경우!
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
visited = [[0] * n for _ in range(n)]
cnt_problem = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt_problem += 1
            
print(cnt_normal, cnt_problem)