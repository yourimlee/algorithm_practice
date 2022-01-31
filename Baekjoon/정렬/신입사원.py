t = int(input())
    
for _ in range(t):
    cnt = 1
    score = []
    
    n = int(input())
    for _ in range(n):
        paper, interview = map(int, input().split())
        score.append([paper, interview])
    
    score.sort()
    max = score[0][1]
    
    for i in range(1, n):
        if max > score[i][1]:
            cnt += 1
            max = score[i][1]
    
    print(cnt)