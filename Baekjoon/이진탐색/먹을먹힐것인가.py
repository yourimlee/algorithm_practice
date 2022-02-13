import sys

t = int(input())

for _  in range(t):
    a, b = map(int, sys.stdin.readline().split())
    alist = list(map(int, sys.stdin.readline().split()))
    blist = list(map(int, sys.stdin.readline().split()))
    blist.sort()
    result = 0
    
    for value in alist:
        start, end = 0, b - 1
        mid = (start + end) // 2
        res = -1
        while start <= end:
            if blist[mid] < value:
                start = mid + 1
                res = max(res, mid)
            else:
                end = mid - 1
        result += res
    print(result)