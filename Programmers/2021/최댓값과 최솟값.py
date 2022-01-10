def solution(s):
    num_list = list(map(int, s.split(' ')))
    min_num = min(num_list)
    max_num = max(num_list)

    return str(min_num) + " " + str(max_num) 
