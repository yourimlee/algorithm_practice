word = input()
alpha = ['c=', 'c-', 'dz=', 'lj', 'nj', 'd-', 's=', 'z=']

for c in alpha:
    if c in word:
        word = word.replace(c, '*')
print(len(word))