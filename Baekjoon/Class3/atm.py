n = int(input())
time = sorted(list(map(int, input().split())), reverse=True)

p = sum([sum(time[t:]) for t in range(len(time))])
print(p)