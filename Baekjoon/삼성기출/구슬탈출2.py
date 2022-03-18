from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

q = deque()

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs():
    init()
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break

        for i in range(4):
            rx_, ry_, r_cnt = move(rx, ry, dx[i], dy[i])
            bx_, by_, b_cnt = move(bx, by, dx[i], dy[i])

            if board[bx_][by_] != 'O':
                if board[rx_][ry_] == 'O':
                    print(depth)
                    return

                if rx_ == bx_ and ry_ == by_:
                    if r_cnt > b_cnt:
                        rx_ -= dx[i]
                        ry_ -= dy[i]
                    else:
                        bx_ -= dx[i]
                        by_ -= dy[i]
                if not visited[rx_][ry_][bx_][by_]:
                    visited[rx_][ry_][bx_][by_] = True
                    q.append((rx_, ry_, bx_, by_, depth + 1))
    print(-1)
    return

bfs()