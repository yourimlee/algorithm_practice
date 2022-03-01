from collections import deque

n, k = map(int, input().split())
max = 1000000
visited = [0] * (max+1)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for j in (x-1, x+1, x*2):
            if 0 <= j <= max and visited[j] == 0:
                visited[j] = visited[x] + 1
                q.append(j)
            
bfs()