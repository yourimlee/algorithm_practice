# 시간초과 날 수 있으니, sys.stdin.readline().split()

import sys
n, m = map(int, sys.stdin.readline().split())

li_1 = list(map(int, sys.stdin.readline().split()))
li_2 = list(map(int, sys.stdin.readline().split()))
res = li_1 + li_2
res = sorted(res)
# 한줄에 모두 출력
print(*res)
