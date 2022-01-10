def solution(clothes):
    answer = 1
    list = {}
    for l in clothes:
        if l[1] not in list:
            list[l[1]] = [l[0]]
        else:
            list[l[1]].append(l[0])
    for key in list:
        answer = answer * (len(list[key])+1)
    return answer-1