def solution(n):
    answer = 0
    for i in range(1, n):
        s = i
        for j in range(i+1, n):
            s += j
            if s == n:
                answer += 1
                break
            elif s>n:
                break
    return answer+1