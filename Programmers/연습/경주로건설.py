from collections import deque
def solution(board):
    answer = 999999
    n = len(board)
    q = deque()
    q.append((0, 0, 4, 0))
    # 0, 1, 2, 3 -> 상, 하, 좌, 우// (x, y, 방향) : cost
    visited = {
        (0, 0, 1) : 0, (0, 0, 3) : 0  # 아래, 오른쪽
    }
    dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]
    while q:
        x, y, d, c = q.popleft()
        if x == n - 1 and y == n - 1:
            answer = min(answer, c)
        for k in range(4):
            nx = x + dx[k]; ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                nc = c
                if d == 4:
                    nc += 100
                elif d <= 1 and k <= 1: # 위 아래
                    nc += 100
                elif d >= 2 and k >= 2: # 왼 오
                    nc += 100
                else: # 방향 바꿀 때
                    nc += 600
                # 방문한적이 없던지, 혹은 방문은 했었지만 cost가 적다면 reset
                if not visited.get((nx, ny, k)) or visited[(nx, ny, k)] > nc:
                    visited[(nx, ny, k)] = nc
                    q.append((nx, ny, k, nc))

    return answer