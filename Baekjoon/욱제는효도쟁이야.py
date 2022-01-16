n = int(input())
k = list(map(int, input().split(' ')))

print(sum(k) - max(k))