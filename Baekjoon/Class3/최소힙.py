import heapq
import sys

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0: print(0)
        else:
            res = heapq.heappop(heap)
            print(res)
    else:
        heapq.heappush(heap, num)