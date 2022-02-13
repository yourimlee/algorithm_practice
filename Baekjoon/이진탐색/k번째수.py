n = int(input())
k = int(input())

start, end = 1, k

while start <= end:
    mid = (start + end) // 2
    res = 0
    for i in range(1, n+1):
        res += min(n, mid // i)
        
    if res < k:
        start = mid + 1
    else:
        end = mid - 1

print(start)