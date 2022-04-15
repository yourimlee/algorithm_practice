r, c = map(int, input().split())
alp = [list(input()) for _ in range(r)]

visited = []
dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]

cnt = 1
def bfs(x, y):
    global cnt
    queue = set([(x, y, alp[x][y])])
    while queue:
        x, y, visit = queue.pop()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and alp[nx][ny] not in visit:
                queue.add((nx, ny, visit + alp[nx][ny]))
                cnt = max(cnt, len(visit) + 1)

bfs(0, 0)
print(cnt)