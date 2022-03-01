w = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in w:
        print(w.index(i), end=' ')
    else:
        print(-1, end = ' ')
        