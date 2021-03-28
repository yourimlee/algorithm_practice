def solution(record):
    dic, log = dict(), list()
    for i in range(len(record)):
        data = record[i].split()
        if data[0] == 'Enter' or data[0] == 'Leave' :
            log.append((data[0], data[1]))
        if data[0] == 'Enter' or data[0] == 'Change' :
            dic[data[1]] = data[2]
    answer = list()

    for state, id in log:
        if state == 'Enter':
            answer.append(dic[id]+'님이 들어왔습니다.')
        else:
            answer.append(dic[id]+'님이 나갔습니다.')
    return answer