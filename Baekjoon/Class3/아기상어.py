import sys
from collections import deque

n = int(input())
loc = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bite_fish(x, y, shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    temp = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]; ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if loc[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    if loc[nx][ny] < shark_size and loc[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))
    return sorted(temp, key = lambda x: (-x[2], -x[0], -x[1]))

dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]
x, y, size = 0, 0, 2
for i in range(n):
    for j in range(n):
        if loc[i][j] == 9:
            x = i
            y = j

cnt = 0
result = 0
while 1:
    shark = bite_fish(x, y, size)
    if len(shark) == 0:
        break
    nx, ny, dist = shark.pop()

    result += dist
    loc[x][y], loc[nx][ny] = 0, 0

    x, y = nx, ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(result)