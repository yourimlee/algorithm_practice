import sys
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] > h and res[nx][ny] == 0:
                res[nx][ny] = 1
                dfs(nx, ny, h)
           
## max(map(max, ...))
ans = 0
for k in range(max(map(max, graph))):
    cnt = 0
    res = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and res[i][j] == 0:
                res[i][j] = 1
                cnt += 1
                dfs(i, j, k)
                
    ans = max(ans, cnt)
    
print(ans)