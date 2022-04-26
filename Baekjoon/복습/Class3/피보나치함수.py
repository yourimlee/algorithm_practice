t = int(input())

def fibonacci(n):
    cnt_zero, cnt_one = [0] * (41), [0] * (41)
    cnt_zero[0] = 1; cnt_one[1] = 1
    for i in range(2, n+1):
        cnt_one[i] = cnt_one[i-2] + cnt_one[i-1]
        cnt_zero[i] = cnt_one[i-1]
    print(cnt_zero[n], cnt_one[n])

for _ in range(t):
    n = int(input())
    fibonacci(n)