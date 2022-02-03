n = int(input())

grades = []
for _ in range(n):
    [a, b, c, d] = input().split()
    grades.append([a, b, c, d])

for i in range(n):
    