def dfs(computers, visit, v):
    if visit[v] == 0:
        visit[v] = 1
        for l in range(len(computers)):
            if computers[v][l] == 1 and visit[l] == 0:
                dfs(computers, visit, l)

def solution(n, computers):
    visit = [0] * n
    answer = 0
    while 0 in visit:
        for i in range(n):
            if visit[i] == 0:
                dfs(computers, visit, i)
                answer += 1
    return answer