t = int(input())
    
def test():
    for i in range(n-1):
        if num[i] == num[i+1][0:len(num[i])]:
            print('NO')
            return
    print('YES')

for _ in range(t):
    n = int(input())
    num = []
    for _ in range(n):
        num.append(str(input()))
    num.sort()
    test()