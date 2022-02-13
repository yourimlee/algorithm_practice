import sys

t = int(input())

def binary():
    n = int(sys.stdin.readline())
    li1 = sorted(list(map(int, sys.stdin.readline().split())))
    m = int(sys.stdin.readline())
    li2 = list(map(int, sys.stdin.readline().split()))
    
    for value in li2:
        start, end = 0, len(li1) - 1
        while start <= end:
            is_found = False
            mid = (start + end) // 2
            if li1[mid] == value:
                is_found = True
                break
            elif li1[mid] < value:
                start = mid + 1
            else:
                end = mid - 1
        print(1 if is_found == True else 0)
        
for _ in range(t):
    binary()
