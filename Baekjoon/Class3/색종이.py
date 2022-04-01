n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

cnt_white, cnt_blue = 0, 0

def dfs(x, y, n):
    global cnt_white, cnt_blue
    num_check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if num_check != paper[i][j]:
                dfs(x, y, n // 2)
                dfs(x, y + n // 2, n // 2)
                dfs(x + n // 2, y, n // 2)
                dfs(x + n // 2, y + n // 2, n // 2)
                return
    if num_check == 1:
        cnt_blue += 1
    elif num_check == 0:
        cnt_white += 1

dfs(0, 0, n)
print(cnt_white)
print(cnt_blue)