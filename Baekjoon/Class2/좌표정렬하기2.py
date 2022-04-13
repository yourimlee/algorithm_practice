n = int(input())
co = []
for _ in range(n):
    x, y = map(int, input().split())
    co.append((x, y))

co.sort(key = lambda x: (x[1], x[0]))
for i in range(len(co)):
    print(co[i][0], co[i][1])