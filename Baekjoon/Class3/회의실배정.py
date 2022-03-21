n = int(input())
time = []
for _ in range(n):
    t1, t2 = map(int, input().split())
    time.append([t1, t2])
time.sort(key = lambda x: (x[1], x[0]))

ans = end = 0
for s, e in time:
    if s >= end:
        ans += 1
        end = e
print(ans)