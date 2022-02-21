def solution(n, lost, reserve):
    lost.sort()
    lost2 = lost.copy()
    for i in lost:        
        if (i in reserve):
            lost2.remove(i)
            reserve.remove(i)
        elif (i-1 in reserve):
            lost2.remove(i)
            reserve.remove(i-1)        
        elif (i+1 in reserve and i+1 not in lost):
            lost2.remove(i)
            reserve.remove(i+1)
    return n - len(lost2)