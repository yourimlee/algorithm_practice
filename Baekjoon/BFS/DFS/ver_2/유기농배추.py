# setrecursionlimit -> recursion error
## graph m(아래) n(오른쪽) 순서이므로, 가로세로 길이가 다를때 반드시 확인해야함.

import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(y, x):
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        for i in range(4):
            dfs(y + dy[i], x + dx[i])
        return True

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * (m) for _ in range(n)]
    for _ in range(k):
        k1, k2 = map(int, input().split())
        graph[k2][k1] = 1
    visited = []
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)