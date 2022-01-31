n, k = map(int, input().split())
num = list(map(int, input().split()))
num_list = sorted(num)

print(num_list[k-1])