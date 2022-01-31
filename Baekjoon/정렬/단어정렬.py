# 퀵 정렬 사용 -> 시간초과
n = int(input())

word = []
for _ in range(n):
    word.append(input())
word = list(set(word))

sort_word = []
for i in word:
    sort_word.append((len(i), i))
result = sorted(sort_word)

for len, word in result:
    print(word)