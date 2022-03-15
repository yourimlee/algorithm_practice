def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]

    dir = 0 # 방향 0 1 2 3
    loop = n
    r, c = 0, -1
    # 시계
    dr_t = [0, 1, 0, -1]
    dc_t = [1, 0, -1, 0]
    # 반시계
    dr_f = [0, -1, 0, 1]
    dr_f = [-1, 0, 1, 0]
    num = 0

    # 최대 채울 수 있는 숫자
    d = [0] * (n + 1)
    d[1], d[2] = 1, 1
    for i in range(3, n+1):
        d[i] = d[i-2] + i-1

    # 홀, 짝 나눠서
    if n % 2 == 1:
        odd = []
        for i in range(1, n+1):
            if i % 2 == 1:
                odd.append(d[i])
        odd = sorted(odd, reverse=True)

    # 숫자 채울 리스트
        # num_ = []
        # for i in range(1, sum(odd)+1):
        #     num_.append(i)
        # num_list = []
            
        while num < n * n:
            for i in range(loop):
                if clockwise == True:
                    r += dr_t[dir]
                    c += dr_t[dir]
                else:
                    r += dr_f[dir]
                    c += dr_f[dir]
                answer[r][c] = num
                num += 1
            dir = (dir + 1) % 4

    else:
        even = []
        for i in range(1, n+1):
            if i % 2 == 0:
                even.append(d[i])
        sorted(even, reverse=True)
        
        while num < n * n:
            for i in range(loop):
                if clockwise == True:
                    r += dr_t[dir]
                    c += dr_t[dir]
                else:
                    r += dr_f[dir]
                    c += dr_f[dir]
                answer[r][c] = num
                num += 1
            dir = (dir + 1) % 4

    return answer