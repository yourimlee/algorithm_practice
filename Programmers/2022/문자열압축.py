def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1):
        c = ''
        cnt = 1
        tmp = s[:i]
        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    c += str(cnt) + tmp
                else:
                    c += tmp
                tmp = s[j:i+j]
                cnt = 1
        if cnt != 1:
            c += str(cnt) + tmp
        else:
            c += tmp

        result.append(len(c))

    return min(result)