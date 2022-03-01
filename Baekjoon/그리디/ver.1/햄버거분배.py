n, k = map(int, input().split())
table = list(input().rstrip())

cnt = 0

for i in range(len(table)):
    if table[i] == "P":
        for j in range(i-k, i+k+1):
            if 0 <= j<n and table[j] == "H":
                cnt += 1
                table[j] = 'nothing'
                break

print(cnt) 