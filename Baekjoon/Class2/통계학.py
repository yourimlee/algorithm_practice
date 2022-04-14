import math
from collections import Counter

n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))
numbers.sort()

print(round(sum(numbers)/len(numbers)))
print(numbers[math.floor(len(numbers)/2)])

cnt = Counter(numbers).most_common()
mode = []
for i in range(len(cnt)):
    if cnt[0][1] == cnt[i][1]: mode.append(cnt[i])
if len(mode) >= 2:
    mode.sort()
    print(mode[1][0])
else:
    print(mode[0][0])

print(numbers[-1] - numbers[0])