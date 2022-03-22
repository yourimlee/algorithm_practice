n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

s = []
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in numbers:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()