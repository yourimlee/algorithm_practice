def solution(msg):
    answer = []
    words = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))
    w = 0
    l = 0
    while True : 
        l += 1
        if msg[w:l+1] not in words:
            words[msg[w:l+1]] = len(words)+1
            answer.append(words[msg[w:l]])
            w = l
        elif l == len(msg):
            answer.append(words[msg[w:l]])
            break

    return answer
