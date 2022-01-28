import sys
sys.setrecursionlimit(10**5)

n = int(input())
# 숫자가 1부터 시작하므로
tree = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def dfs(s):
    for i in tree[s]:
        if parents[i] == 0:
            parents[i] = s
            dfs(i)
    
dfs(1)
for i in range(2, n+1):
    print(parents[i])