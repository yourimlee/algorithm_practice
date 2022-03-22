n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, len(numbers)):
        s.append(numbers[i])
        dfs(i)
        s.pop()

dfs(0)