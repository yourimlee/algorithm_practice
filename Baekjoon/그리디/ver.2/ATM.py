n = int(input())
time = list(map(int, input().split()))
time.sort()

for i in range(1, len(time)):
    time[i] = time[i-1] + time[i]
    
print(sum(time))