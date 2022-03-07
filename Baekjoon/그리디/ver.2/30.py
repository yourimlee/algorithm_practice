n = list(map(int, str(input())))
n.sort(reverse = True)

if 0 not in n:
    print(-1)
else:
    if sum(n) % 3 != 0:
        print(-1)
    else:
        print(''.join(str(x) for x in n))