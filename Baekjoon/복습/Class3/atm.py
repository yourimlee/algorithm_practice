from time import time


n = int(input())
p = sorted(list(map(int, input().split())))

time = 0
for i in range(len(p)):
    time += sum(p[:i+1])
print(time)