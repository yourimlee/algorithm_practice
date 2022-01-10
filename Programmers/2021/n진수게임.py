def trans(n, num):
    arr = "0123456789ABCDEF"
    res = ''
    if num == 0:
        return '0'
    while num > 0:
        res = arr[num%n] + res
        num = num // n
    return res

def solution(n, t, m, p):
    answer = ''
    str = ''
    for i in range(t * m):
        str += trans(n, i)
    for s in range(p-1, t*m, m):
        answer += str[s]
    return answer