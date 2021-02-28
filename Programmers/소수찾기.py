from itertools import permutations
# find prime
def prime(num_list):
    prime = 0
    for n in num_list:
        count = 0   
        for i in range(2, n):
            if n % i == 0 :
                count += 1
                break
        if n > 1 and count == 0 :
            prime += 1
    return prime

# 만들 수 있는 number list(permutation module 사용)
def solution(numbers):
    numb_list = []
    for i in range(1, len(numbers)+1):
        nPr = permutations(numbers, i)
        for n in nPr:
            nPr_ = "".join(n)
            numb_list.append(int(nPr_))
    num_list = set(numb_list)
    return prime(num_list)