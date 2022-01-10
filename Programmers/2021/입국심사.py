def solution(n, times):
    answer = 0
    number = len(times)
    start, end = 1, n*max(times)

    while start <= end:
        mid = (start+end)//2
        cnt = 0
        for time in times:
            cnt += mid//time
            if cnt >= n:
                break
        
        if cnt >= n:
            answer = mid
            end = mid - 1
        elif cnt < n:
            start = mid + 1
    return answer