k = int(input())
zero = []

for i in range(k):
    num = int(input())
    if num == 0:
        zero.pop()
    else:
        zero.append(num)
print(sum(zero))