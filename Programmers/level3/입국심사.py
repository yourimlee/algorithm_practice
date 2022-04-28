def solution(n, times):
    start, end = 1, n * max(times)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for time in times:
            cnt += mid // time

        if cnt >= n:
            end = mid - 1
        else:
            start = mid + 1

    return start