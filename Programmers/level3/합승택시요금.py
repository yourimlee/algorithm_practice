# 플로이드와샬

def solution(n, s, a, b, fares):
    inf = 10000000
    answer = inf
    graph = [[inf] * n for _ in range(n)]

    for n1, n2, fee in fares:
        graph[n1-1][n2-1] = graph[n2-1][n1-1] = fee

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                else:
                    graph[i][j] = 0

    for t in range(n):
        temp = graph[s-1][t] + graph[t][a-1] + graph[t][b-1]
        answer = min(temp, answer)

    return answer