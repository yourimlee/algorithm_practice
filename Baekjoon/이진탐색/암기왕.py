import sys

# 리스트 순번으로 이진탐색
def bin(li1, i):
    start, end = 0, len(li1) - 1
    mid = (start + end) // 2
    while start <= end:
        if li1[mid] == i:
            return 1
        elif li1[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    return 0
        
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li1 = list(map(int, sys.stdin.readline().split()))
    li1.sort()
    m = int(sys.stdin.readline())
    li2 = list(map(int, sys.stdin.readline().split()))
    for i in li2:
        print(bin(li1, i))
