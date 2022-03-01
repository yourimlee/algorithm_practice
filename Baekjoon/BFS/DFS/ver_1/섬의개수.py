import sys
sys.setrecursionlimit(10000)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(x, y):
    if 0 <= x < h and 0 <= y < w:
        if graph[x][y] == 1:
            graph[x][y] = 2
            ## 같은 것으로 인식하고 count = 인접한 것은 모두 true
            # 이렇게 해도 됨.
            # for i in range(8):
            #     dfs(x + dx[i], y + dy[i])
            dfs(x-1, y-1)
            dfs(x-1, y)
            dfs(x-1, y+1)
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y-1)
            dfs(x+1, y)
            dfs(x+1, y+1)
            return True
        return False

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
         