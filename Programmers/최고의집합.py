def solution(n, s):
    answer = []

    if s // n <1:
        answer = [-1]
    else:
        n1 = s // n

        for i in range(n):
            answer.append(n1)
        n2 = s % n
        id = len(answer) - 1

        for i in range(n2):
            answer[id-i] = answer[id-i] + 1
    
    return answer