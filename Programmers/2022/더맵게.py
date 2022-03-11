import heapq
from tarfile import _Bz2ReadableFileobj
def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)
    while 1:
        if len(scoville) <= 1 and scoville[0] < k:
            answer = -1
            break
        if scoville[0] >= k:
            break
        new = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new)
        answer += 1
    
    return answer
    
print(solution([1,2,3,9,10,12], 7))