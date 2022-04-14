import sys

n = int(sys.stdin.readline())
sang = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
diff = list(map(int, sys.stdin.readline().split()))

cnt_num = {}
for s in sang:
    if s in cnt_num:
        cnt_num[s] += 1
    else: cnt_num[s] = 1

for num in diff:
    result = cnt_num.get(num)
    if result == None: print(0, end=' ')
    else:
        print(result, end = ' ')