from datetime import datetime
from collections import defaultdict
import math

def solution(fees, records):
    answer = []; rec = {}
    for r in records:
        t, n, i = r.split(); h, m = t.split(':')
        time = int(h) * 60 + int(m)
        if n not in rec:
            rec[n] = list(); rec[n].append(time)
        else:
            rec[n].append(time)
    # out이 기록되지 않은 곳에 23:59를 추가
    result = sorted(rec.items())
    for i in range(len(result)):
        if len(result[i][1]) % 2 == 1:
            result[i][1].append(1439)
    # 요금계산
    for k in range(len(result)):
        diff = 0; money = 0
        for l in range(0, len(result[k][1]), 2):
            diff += result[k][1][l+1] - result[k][1][l]
        if diff < fees[0]: money += fees[1]
        else:
            money += fees[1] + math.ceil((diff - fees[0]) / fees[2]) * fees[3]
        answer.append(money)

    return answer