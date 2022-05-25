import sys
from collections import deque

t = int(input())

for _ in range(t):
    test = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    q = deque(arr)

    flag = 0
    if n == 0:
        q = []

    for j in test:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(q) != 0:
                if flag % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                print('error')
                break

    else:
        if flag % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
