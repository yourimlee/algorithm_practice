from collections import deque

def bfs(p):
    start = []
    for j in range(5):
        for i in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    for s in start:
        queue = deque([s])
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[s[0]][s[1]] = 1

        while queue:
            x, y = queue.popleft()
            dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]
            for i in range(4):
                nx = x + dx[i]; ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:

                    if p[nx][ny] == 'O':
                        queue.append([nx, ny])
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[x][y] + 1

                    if p[nx][ny] == 'P' and distance[x][y] <= 1:
                        return 0

    return 1

def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))

    return answer