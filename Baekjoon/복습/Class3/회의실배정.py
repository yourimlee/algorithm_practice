n = int(input())
time = []
for _ in range(n):
    a, b = map(int, input().split())
    time.append([a, b])
time.sort(key = lambda x: (x[1], x[0]))

ans = end = 0
for s, e in time:
    if s >= end:
        ans += 1
        end = e
print(ans)