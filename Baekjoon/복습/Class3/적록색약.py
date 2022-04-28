from collections import deque

dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]
def bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append([x, y])
    word = graph[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if graph[nx][ny] == word:
                    q.append([nx, ny])
                    visited[nx][ny] = 1

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnt_normal = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt_normal += 1

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
cnt_ill = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt_ill += 1

print(cnt_normal, cnt_ill)