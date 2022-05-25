import sys

target = int(sys.stdin.readline())
n = int(sys.stdin.readline())
broken = list(map(int, sys.stdin.readline().split()))
min_cnt = abs(100 - target)

for num in range(1000001):
    num = str(num)

    for j in range(len(num)):
        if int(num[j]) in broken:
            break
        elif j == len(num) - 1:
            min_cnt = min(min_cnt, abs(int(num) - target) + len(num))

print(min_cnt)