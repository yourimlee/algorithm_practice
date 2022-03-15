## bfs, dfs 문제

from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    while queue:
        tar, id = queue.popleft()
        id += 1
        if id < len(numbers):
            queue.append([tar + numbers[id], id])
            queue.append([tar - numbers[id], id])
        else:
            if tar == target:
                answer += 1
                
    return answer