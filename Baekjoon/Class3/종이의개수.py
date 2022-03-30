n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt_minus, cnt_zero, cnt_plus = 0, 0, 0

def dfs(x, y, n):
    global cnt_minus, cnt_zero, cnt_plus
    num_check = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num_check:
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * n // 3, y + l * n // 3, n // 3)
                return

    if num_check == -1:
        cnt_minus += 1
    if num_check == 0:
        cnt_zero += 1
    if num_check == 1:
        cnt_plus += 1

dfs(0, 0, n)
print(cnt_minus)
print(cnt_zero)
print(cnt_plus)