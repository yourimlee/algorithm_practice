n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
tar = list(map(int, input().split()))

def binary(array, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

for i in tar:
    res = binary(array, i, 0, n-1)
    if res != None:
        print(1)
    else:
        print(0)
