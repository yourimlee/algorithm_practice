k, n = map(int, input().split())
length = []
for _ in range(k):
    length.append(int(input()))

start, end = 1, max(length)

while start <= end:
    mid = (start + end) // 2
    res = 0
    for i in length:
        res += (i // mid)
        
    if res >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end) 