from collections import deque

n = int(input())
queue = deque()
for i in range(1, n+1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    num = queue.popleft()
    queue.append(num)

print(queue[0])