n = int(input())

num = 1
while (num * (num+1) / 2) <= n:
    num += 1

print(num-1)