n = int(input())

nums = []
for i in range(n):
    [a, b] = map(int, input().split())
    nums.append([a, b])
    
nums = sorted(nums)
for i in range(n):
    print(nums[i][0], nums[i][1])