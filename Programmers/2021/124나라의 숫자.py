def solution(n):
    answer = ''
    number = {1:'1', 2:'2', 0:'4'}
    p=1
    q=1
    while p != 0:
        p=n//3
        q=n%3
        if q==0:
            p-=1
        n=p
        answer=number[q]+answer
    return answer
