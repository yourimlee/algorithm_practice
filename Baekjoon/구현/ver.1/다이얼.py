w = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

res = 0

for i in range(len(w)):
    for j in dial:
        if w[i] in j:
            res += dial.index(j)+3
            
print(res)