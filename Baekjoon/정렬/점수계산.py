scores = {}
for i in range(1, 9):
    k = int(input())
    scores[i] = k
scores = sorted(scores.items(), key = lambda x:x[1], reverse = True)
n, s = [], []

for num, score in scores[:5]:
    n.append(num)
    s.append(score)
n = sorted(n)

print(sum(s))
print(*n)
