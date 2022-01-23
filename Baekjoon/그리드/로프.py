n = int(input())
weight = []
for i in range(n):
    weight.append(int(input()))

weight.sort(reverse=True)
new = []
for i in range(len(weight)):
    new.append(weight[i] * (i+1))

print(max(new))