def solution(arr1, arr2):
    answer = []
    for a in range(len(arr1)):
        row = []
        for b in range(len(arr2[0])):
            cnt = 0
            for c in range(len(arr1[0])):
                cnt += arr1[a][c] * arr2[c][b]
            row.append(cnt)
        answer.append(row)
        
    return answer