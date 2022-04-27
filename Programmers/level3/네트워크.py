from collections import deque

def bfs(n, computers, com, visited):
    q = deque()
    q.append(com)
    visited[com] = 1
    while q:
        com = q.pop()
        visited[com] = 1
        for i in range(n):
            if i != com and computers[com][i] == 1 and visited[i] == 0:
                q.append(i)

def solution(n, computers):
    cnt = 0
    visited = [0] * n
    for com in range(n):
        if visited[com] == 0:
            bfs(n, computers, com, visited)
            cnt += 1
    return cnt