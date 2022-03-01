num = int(input())
data = list(map(int, input().split()))
data.sort()

## 앞에 시간에 더하기해서 리스트 요소값 바꾸기
for i in range(1, num):
    data[i] += data[i-1]
        
print(sum(data))


