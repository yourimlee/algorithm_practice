def solution(citations):
    citations.sort()
    answer = 0
    h = 0
    k = 0
    for i in range(1, len(citations)):
        h = sum(j >= i for j in citations)
        k = sum(j <= i for j in citations)
        if h >= i and k <= i:
            if i > answer:
                answer = i
    if citations[0] >= len(citations):
        answer = len(citations)
    return answer