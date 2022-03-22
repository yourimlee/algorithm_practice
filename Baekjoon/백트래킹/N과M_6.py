n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, len(numbers)):
        if numbers[i] not in s:
            s.append(numbers[i])
            dfs(i+1)
            s.pop()

dfs(0)