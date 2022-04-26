n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse = True)

cnt = 0
for c in range(len(coin)):
    cnt += k // coin[c]
    k %= coin[c]
print(cnt)