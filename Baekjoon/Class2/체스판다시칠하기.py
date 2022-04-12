n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
chess = []

for i in range(n-7):
    for j in range(m-7):
        id1 = 0; id2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W': id1 += 1
                    if board[a][b] != 'B': id2 += 1
                else:
                    if board[a][b] != 'B': id1 += 1
                    if board[a][b] != 'W': id2 += 1
        chess.append(id1)
        chess.append(id2)

print(min(chess))