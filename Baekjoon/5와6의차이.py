n, m = map(str, input().split())

a = n.replace('6', '5')
b = m.replace('6', '5')
c = n.replace('5', '6')
d = m.replace('5', '6')

sum1 = int(a) + int(b)
sum2 = int(c) + int(d)

print(sum1, sum2)
