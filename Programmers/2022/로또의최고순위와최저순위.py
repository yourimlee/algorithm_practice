def solution(lottos, win_nums):
    answer = []
    cnt = lottos.count(0)
    if 0 in lottos:
        lottos.remove(0)
    res = 0
    for lotto in lottos:
        if lotto in win_nums:
            res += 1
            
    if res == 0 or res == 1:
        res_min = 6
    else:
        res_min = 7 - res
    if cnt == 6:
        res_max = 1
    else:
        res_max = res_min - cnt
    answer.append(res_max)
    answer.append(res_min)
    
    return answer