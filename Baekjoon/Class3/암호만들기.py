import sys

l, c = map(int, sys.stdin.readline().split())
alpha = sorted(list(sys.stdin.readline().split()))
visit = [0] * c
code = []

def dfs(k, next, v):
    global cnt_v, cnt_n
    if k == l:
        if v and len(code) - v > 1:
            print(''.join(code))
        return

    for i in range(next, c):
        if visit[i] == 0:
            visit[i] = 1
            code.append(alpha[i])

            if alpha[i] in 'aeiou':
                dfs(k+1, i+1, v+1)
            else:
                dfs(k+1, i+1, v)

            visit[i] = 0
            code.pop()

dfs(0, 0, 0)