def solution(v):
    answer = []
    x, y = [], []
    for i in range(3):
        x.append(v[i][0])
        y.append(v[i][1])
    x.sort(), y.sort()
    
    if x[0] == x[1]:
        answer.append(x[-1])
    else:
        answer.append(x[0])
    
    if y[0] == y[1]:
        answer.append(y[-1])
    else:
        answer.append(y[0])
    
    return answer

# print(solution([[1, 4], [3, 4], [3, 10]]))
print(solution([[1, 1], [2, 2], [1, 2]]))