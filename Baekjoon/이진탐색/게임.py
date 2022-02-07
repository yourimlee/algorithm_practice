x, y = map(int, input().split())
z = (y * 100) // x

if z >= 99:
    print(-1)
else:
    start, end = 1, int(x)
    game = 0
    while start <= end:
        mid = (start + end) // 2
        if (y + mid) * 100 // (x + mid) <= z:
            start = mid + 1
        else:
            game = mid
            end = mid - 1

    print(game)    