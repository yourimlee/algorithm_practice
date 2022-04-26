from collections import deque

n = int(input())
map = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]
def bfs(x, y):
    cnt = 1
    if map[x][y] == 1:
        map[x][y] = 0
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and map[nx][ny] == 1:
                    map[nx][ny] = 0
                    cnt += 1
                    q.append((nx, ny))
    return cnt

cnt_sum = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            cnt_sum.append(bfs(i, j))

cnt_sum.sort()
print(len(cnt_sum))
for c in cnt_sum:
    print(c)
