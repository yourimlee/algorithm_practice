n = int(input())

answer = []
stack = []
no_num = 0
inp = 1
for i in range(n):
    num = int(input())
    while inp <= num:
        stack.append(inp)
        answer.append('+')
        inp += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        no_num = 1
        break

if no_num == 0:
    for i in answer:
        print(i)