def solution(answers):
    answer = []
    res = {1 : 0, 2 : 0, 3 : 0}
    ans_1 = [1,2,3,4,5] * 2000
    ans_2 = [2,1,2,3,2,4,2,5] * 1250
    ans_3 = [3,3,1,1,2,2,4,4,5,5] * 1000

    for i in range(len(answers)):
        if answers[i] == ans_1[i]: res[1] += 1
        if answers[i] == ans_2[i]: res[2] += 1
        if answers[i] == ans_3[i]: res[3] += 1

    res = sorted(res.items(), key = lambda x : (-x[1], x[0]))

    answer.append(res[0][0])
    if res[0][1] == res[1][1]: answer.append(res[1][0])
    if res[0][1] == res[2][1]: answer.append(res[2][0])

        
    return answer
