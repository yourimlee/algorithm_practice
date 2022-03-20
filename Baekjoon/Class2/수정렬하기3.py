import sys

n = int(input())
checklist = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    checklist[num] += 1

for i in range(10001):
    if checklist[i] != 0:
        for _ in range(checklist[i]):
            print(i)