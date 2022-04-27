from collections import deque

dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]
def bfs(x, y, loc, visited):
    visited[x][y] = 1
    if loc[x][y] == 1:
        loc[x][y] = 0
    for l in range(4):
        nx = x + dx[l]; ny = y + dy[l]
        if 0 <= nx < n and 0 <= ny < m and loc[nx][ny] == 1 and visited[nx][ny] == 0:
            loc[nx][ny] = 0
            bfs(nx, ny, loc, visited)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    loc = [[0] * (m) for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        loc[b][a] = 1
    cnt = 0
    visited = [[0] * (m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if loc[i][j] == 1:
                cnt += 1
                bfs(i, j, loc, visited)
    print(cnt)