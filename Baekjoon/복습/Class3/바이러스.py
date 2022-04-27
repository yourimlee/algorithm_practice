n = int(input())
m = int(input())
virus = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    virus[a][b] = virus[b][a] = 1

result = []
def dfs(v):
    for i in range(n+1):
        if virus[v][i] == 1 and i not in result:
            result.append(i)
            dfs(i)
    return len(result) - 1

print(dfs(1))