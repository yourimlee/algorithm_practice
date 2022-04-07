from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for num in course:
        course_list = []
        for i in orders:
            if len(i) >= num:
                course_list.extend((list(combinations(sorted(list(i)), num))))
        course_cnt = Counter(course_list).most_common()
        if len(course_cnt) >= 1 and course_cnt[0][1] >= 2:
            for i in range(len(course_cnt)):
                if course_cnt[0][1] == course_cnt[i][1]:
                    c = ''.join(course_cnt[i][0])
                    answer.append(c)
                    answer.sort()
    
    return answer