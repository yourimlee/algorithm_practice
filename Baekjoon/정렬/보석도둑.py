## 이진트리 할때 다시 풀기!

n, k = map(int, input().split())

jewel = []
for _ in range(n):
    # m이 무게, v가 가격
    [m, v] = map(int, input().split())
    jewel.append([m, v]) 
jewel.sort()

bag = []
# 최대로 담을 수 있는 가방무게
for _ in range(k):
    bag.append(int(input()))
bag.sort()
