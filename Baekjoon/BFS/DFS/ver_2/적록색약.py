from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = 1

cnt_0 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt_0 += 1
    
# 적록색맹 그래프 수정
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
visited = [[0] * n for _ in range(n)]
cnt_1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt_1 += 1
            
print(cnt_0, cnt_1)