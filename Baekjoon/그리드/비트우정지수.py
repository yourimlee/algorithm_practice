## 다시 풀기!

t = int(input())
n, m = input().split()

for _ in range(t) :
  cnt_1 = 0
  cnt_0 = 0

  for i in range(len(m)) :
    if n[i] != m[i] :
      if m[i] == '1' :
        cnt_1 += 1
      else :
        cnt_0 += 1

  print(max(cnt_1, cnt_0))