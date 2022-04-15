n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

cnt_0, cnt_1 = 0, 0
def dfs(x, y, n):
    global cnt_0, cnt_1
    num_check = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != num_check:
                dfs(x, y, n // 2)
                dfs(x + n // 2, y, n // 2)
                dfs(x, y + n // 2, n // 2)
                dfs(x + n // 2, y + n // 2, n // 2)
                return
    if num_check == 0: cnt_0 += 1
    if num_check == 1: cnt_1 += 1

dfs(0, 0, n)
print(cnt_0)
print(cnt_1)