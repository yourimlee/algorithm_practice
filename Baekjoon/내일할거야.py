case = int(input())

arr = []

for _ in range(case):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x: x[1] ,reverse=True)

time = arr[0][1]-arr[0][0]+1

for i in range(1,len(arr)):
    if arr[i][1]>= time:
        time = arr[i][1] - arr[i][0] - (arr[i][1] - time)
    else:
        time = arr[i][1] - arr[i][0] + 1

print(time-1)