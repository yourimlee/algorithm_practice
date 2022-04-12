import sys
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
ops = list(map(int, sys.stdin.readline().split()))
max_num, min_num = -1e9, 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global max_num, min_num
    if depth == n:
        max_num = max(total, max_num)
        min_num = min(total, min_num)

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)

dfs(1, num[0], ops[0], ops[1], ops[2], ops[3])
print(max_num)
print(min_num)