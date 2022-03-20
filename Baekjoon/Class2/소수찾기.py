n = int(input())
numbers = list(map(int, input().split()))

max_n = max(numbers)
cnt = n
for num in numbers:
    if num == 1:
        cnt -= 1
    else:
        for i in range(2, max_n):
            if num != i:
                if num % i == 0:
                    cnt -= 1
                    break

print(cnt)