import sys
from itertools import combinations

while True:

    stack = list(map(int, sys.stdin.readline().split()))
    if stack[0] == 0: break
    del stack[0]
    s = list(combinations(stack, 6))
    for i in s:
        for j in i:
            print(j, end = ' ')
        print()
    print()