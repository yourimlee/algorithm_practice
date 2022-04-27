from collections import deque

n, k = map(int, input().split())
max = 1000000
visited = [0] * 10000001

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i < max and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)
bfs()