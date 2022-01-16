## 다시 풀기!

T = int(input())

for _ in range(T):
    n = int(input())
    card = list(map(str, input().split()))
    res = card[0]
    for i in range(1, len(card)):
        left, right = res[0], res[-1]
        
        if card[i] <= left:
            res = res + card[i]
        else:
            res = card[i] + res

print(res)