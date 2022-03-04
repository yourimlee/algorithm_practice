def solution(id_list, report, k):
    dic1, dic2, cnt = {}, {}, {}
    report = list(set(report))
    for id in id_list:
        cnt[id] = 0
    for id in report:
        user_1, rep = id.split(' ')[0], id.split(' ')[1] 
        if user_1 not in dic1:
            dic1[user_1] = []
            dic1[user_1].append(rep)
        else:
            dic1[user_1].append(rep)
    for id in report:
        user_1, rep = id.split(' ')[0], id.split(' ')[1] 
        if rep not in dic2:
            dic2[rep] = 1
        else:
            dic2[rep] += 1
    for id in id_list:
        if id in dic1:
            for i in range(len(dic1[id])):
                if dic2[dic1[id][i]] >= k:
                    cnt[id] += 1
        
    return cnt, list(cnt.values())