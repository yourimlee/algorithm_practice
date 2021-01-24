def solution(n, lost, reserve):
    reserve_set=[r for r in reserve if r not in lost]
    lost_set=[l for l in lost if l not in reserve]
    for r in reserve_set:
        if r-1 in lost_set:
            lost_set.remove(r-1)
        elif r+1 in lost_set:
            lost_set.remove(r+1)
    return n-len(lost_set)
