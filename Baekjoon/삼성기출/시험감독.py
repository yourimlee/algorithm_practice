import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

answer = n
for num in a:
    if num >= b:
        answer += math.ceil((num - b) / c)

print(answer)