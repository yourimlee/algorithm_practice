t = int(input())

def printer(w, m):
    cnt = 0
    while True:
        max_w = max(w)
        for i in range(len(w)):
            if w[i] == max(w):
                cnt += 1
                w[i] = 0
                max_w = max(w)
                if i == m:
                    return cnt

for _ in range(t):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    print(printer(w, m))