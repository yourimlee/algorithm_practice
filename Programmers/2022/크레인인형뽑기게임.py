def solution(board, moves):
    answer = 0
    bucket = []
    for num in moves:
        for i in range(len(board)):
            if board[i][num-1] != 0:
                bucket.append(board[i][num-1])
                board[i][num-1] = 0
                if len(bucket) > 1:
                    if bucket[-2] == bucket[-1]:
                        bucket.pop(-1)
                        bucket.pop(-1)
                        answer += 2
                break

    return answer