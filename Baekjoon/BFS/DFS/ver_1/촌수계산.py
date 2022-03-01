from collections import deque

n = int(input())
s, e = map(int, input().split())
m = int(input())

family = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    c, d = map(int, input().split())
    family[c].append(d)
    family[d].append(c)

def bfs(start, end):
    cnt = 0
    q = deque([[start, cnt]])
    while q:
        value = q.popleft()
        start = value[0]
        cnt = value[1]
        if start == end:
            return cnt
        if visited[start] == 0:
            cnt += 1
            visited[start] = 1
            for i in family[start]:
                if visited[i] == 0:
                    q.append([i, cnt])
    return -1
    
print(bfs(s, e))