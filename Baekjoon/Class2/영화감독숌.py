n = int(input())

num_list = []
for i in range(666, 3366666):
    if str(i).count('666') >= 1:
        num_list.append(i)
print(num_list[n-1])