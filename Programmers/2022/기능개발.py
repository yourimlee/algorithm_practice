import math
def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        days.append(int(math.ceil((100 - progresses[i]) / speeds[i])))
    
    cnt = 0
    for i in range(len(days)):
        if days[i] > days[cnt]:
            answer.append(i - cnt)
            cnt = i
    answer.append(len(days) - cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))