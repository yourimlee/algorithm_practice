# 맨날 미루다가 조합 모듈 써봄
from itertools import combinations
# 중복 개수를 세는 모듈
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        list = []
        for order in orders:
            comb = combinations(sorted(order), c)
            list += comb
        count = Counter(list)
        # 메뉴 조합이 있어야 하고 2인이상 시켜야 메뉴를 주문했어야 한다.
        if len(count) != 0 and max(count.values()) != 1:
            answer += [''.join(l) for l in count if count[l] == max(count.values())]

    return sorted(answer)