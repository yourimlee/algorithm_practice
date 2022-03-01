n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for i in word:
        print(i * int(cnt), end='')
    print() # 줄 넘기기
