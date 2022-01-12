num = int(input())
cnt = 0

## 무게가 5로 나눠지면 바로 몫을 프린트하고, 나눠지지않으면 3을 빼고 cnt에 1을 더한다. 그리고 계속 반복.
while num >= 0:
    if num % 5 == 0:
        cnt += num // 5
        print(cnt)
        break
    
    num -= 3
    cnt += 1
else:
    print(-1)
