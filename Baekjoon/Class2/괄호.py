n = int(input())
for _ in range(n):
    data = input()
    vps = []
    
    for c in data:
        if c == '(':
            vps.append(c)
        elif c == ')':
            if len(vps) != 0 and vps[-1] == '(':
                vps.pop()
            else:
                vps.append(c)
                break
    
    if len(vps) == 0:
        print('YES')
    else:
        print("NO")