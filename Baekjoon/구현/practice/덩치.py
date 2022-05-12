n = int(input())
people = []
for _ in range(n):
    w, h = map(int, input().split())
    people.append((w, h))
ranks = []
for c in people:
    rank = 1
    for n in people:
        if (c[0] != n[0]) and (c[1] != n[1]):
            if c[0] < n[0] and c[1] < n[1]:
                rank += 1
    ranks.append(rank)

for r in ranks:
    print(r, end = ' ')