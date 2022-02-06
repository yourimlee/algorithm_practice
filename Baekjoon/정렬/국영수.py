n = int(input())

grades = []
for _ in range(n):
    [name, a, b, c] = map(str, input().split())
    grades.append([name, int(a), int(b), int(c)])

## 정렬 방식
### sorted(key=lambda ~~~) 
### 내림차순은 sorted(key=lambda x:-x[0])

grades = sorted(grades, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for name in grades:
    print(name[0])