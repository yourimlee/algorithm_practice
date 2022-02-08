import sys
# 입국심사대, 총인원
n, m = map(int, sys.stdin.readline().split())
time = []
for _ in range(n):
    time.append(int(sys.stdin.readline()))

start, end = 1, m * max(time)
while start <= end:
    mid = (start + end) // 2
    res = 0
    for t in time:
        res += mid // t
    if res >= m:
        end = mid - 1
    else:
        start = mid + 1

print(start)