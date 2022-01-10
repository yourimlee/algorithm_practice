import math

def solution(progresses, speeds):
    answer = []
    result = []
    for i in range(len(progresses)):
        a = math.ceil((100 - progresses[i])/speeds[i])
        result.append(a)
    comp = 0
    for idx in range(len(result)):
        if result[idx] > result[comp]:
            answer.append(idx-comp)
            comp = idx
    answer.append(len(result)-comp)

    return answer