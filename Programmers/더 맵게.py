import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while 1:
        if len(scoville) <= 1 and scoville[0] < K:
            answer = -1
            break
        if scoville[0] >= K:
            break
        new = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, new)
        answer +=1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))

'''
# 이 코드는 예시는 통과하는데 효율성에서 통과 못함.. 
## 알아보니 heap module을 쓰지 않으면 안된다고 함 ㅠㅠ

def solution(scoville, K):
    answer = 0
    while True:
        sorted(scoville)
        if scoville[0] < K:
            scoville[0] = scoville[0] + scoville[1] * 2
            del scoville[1]
            answer += 1
        else:
            break

    return answer
'''