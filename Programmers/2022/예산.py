def solution(d, budget):
    answer = 0
    d.sort()
    while budget > 0 and len(d) >= 1:
        budget -= d[0]
        if budget >= 0:
            answer += 1
        del d[0]

    return answer