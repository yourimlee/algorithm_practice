from collections import deque
def bfs(begin, target, words, visited):
    q = deque()
    q.append([begin, 0])
    while q:
        cur, depth = q.popleft()
        if cur == target:
            return depth
        for i in range(len(words)):
            if visited[i] == 1: continue
            cnt = 0
            for a, b in zip(cur, words[i]):
                if a != b: cnt += 1
            if cnt == 1:
                visited[i] = 1
                q.append([words[i], depth + 1])

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return(0)
    visited = [0] * len(words)
    answer = bfs(begin, target, words, visited)
    return answer