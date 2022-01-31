word = list(input())

words = []
for i in range(len(word)):
    words.append(''.join(word[i:]))
    
words = sorted(words)

for i in words:
    print(i)