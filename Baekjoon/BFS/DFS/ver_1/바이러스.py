com = int(input())
link = int(input())
# 문제에서는 숫자가 1부터 시작이고, 원래는 0부터
matrix = [[0] * (com + 1) for i in range(com + 1)]
visited = [0] * (com + 1)

for _ in range(link):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
    
result = []

# 1번 컴퓨터에 의해 걸리는 컴퓨터 개수 구하기
def dfs(v):
    visited[v] = 1
    for i in range(1, com + 1):
        if matrix[v][i] == 1 and visited[i] == 0:
            result.append(i)
            dfs(i)
    return len(result)
    
print(dfs(1))