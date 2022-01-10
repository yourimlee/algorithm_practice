import math

def solution(n, k):
    answer = []
    num_list = [i for i in range(1, n+1)]
    while (n != 0):
        tmp = math.factorial(n) // n # 한개에 몇개씩의 값이 있을지 알 수 잇음.
        index = k // tmp
        k = k % tmp
        if k == 0:
            answer.append(num_list.pop(index-1))
        else :
             answer.append(num_list.pop(index))

        n -= 1
    
    return answer