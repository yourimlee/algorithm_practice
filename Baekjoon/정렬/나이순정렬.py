n = int(input())

member = []
for _ in range(n):
    age, name = map(str, input().split())
    member.append([int(age), name])

## lambda 함수 이용
member.sort(key = lambda x: int(x[0]))

for i in member:
    print(i[0], i[1])