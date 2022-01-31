nums = list(map(int, str(input())))

nums = sorted(nums, reverse = True)
## 정수형인 경우에는, 모두 string으로 변경한 후에 join
print(''.join(str(_) for _ in nums))