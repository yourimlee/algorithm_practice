## 다시풀기!

but = list(map(int, input().split()))
n = int(input())
f = list(map(int, input().split()))

cnt = 0
push = []
push.append(abs(but[0]-but[1]))
for i in range(len(f)):
    if f[i] == but[1]:
        cnt += 1
        push.append(int(0))
    else:
        push.append(abs(f[i]-but[1]))
        cnt += 1
        
cnt += min(push)
            