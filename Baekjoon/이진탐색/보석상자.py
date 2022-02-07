import sys
input = sys.stdin.readline

n, m = map(int, input().split())
color = []
for _ in range(m):
    color.append(int(input()))
    
start, end = 1, max(color)

while start <= end:
    # 한 사람이 가져가는 보석의 수, mid로 탐색
    mid = (start + end) // 2
    res = 0
    for i in color:
        if i % mid == 0:
            res += i // mid
        else:
            res += i // mid + 1
## 단순하다. 원래 사람수보다 크면 더 많이씩 가져가야하니까 mid가 커져야함. 고로 시작점이 증가.
    if res > n:
        start = mid + 1
    else:
        end = mid - 1
        
print(start)