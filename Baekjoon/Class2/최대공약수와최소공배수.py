m, n = map(int, input().split())

num = 1
for i in range(1, min(m, n)+1):
    if (m % i == 0) and (n % i == 0):
        num = i
        a = int(m / num); b = int(n / num)

print(num)
print(int(num * a * b))