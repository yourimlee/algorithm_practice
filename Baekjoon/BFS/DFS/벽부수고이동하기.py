## 이 문제 다시 한번 꼭 풀어보기.. 이거 너무 어렵다ㅠㅠㅠ
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
## 3차원 배열 만들기 / 1이라면 벽을 뚫을 수 있는 상태! [x좌표, y좌표, [방문, 벽뚫기여부]]
visited = [[[0] * 2 for i in range(m)] for i in range(n)]
def bfs():
    q = deque()
    q.append([0, 0, 1])
    visited[0][0][1] = 1
    while q:
        x, y, z = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽이 있고, 뚫을 수 있는 경우
                if graph[nx][ny] == 1 and z == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append([nx, ny, 0])
                # 이동할 수 있고, 방문안했고, 벽 뚫을 수 없는 경우
                elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append([nx, ny, z])
                    
    return -1
                    
print(bfs)