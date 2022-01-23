time = int(input())

## 일단 10의 배수가 맞는지 확인하고, 300, 60, 10 차례로 몫과 나머지로 계산해서 코드짜기
if time % 10 != 0:
    print(-1)
else:
    a = 0
    b = 0
    c = 0
    a = time // 300
    b = (time % 300) // 60
    c = ((time % 300) % 60) // 10
    print(a, b, c)