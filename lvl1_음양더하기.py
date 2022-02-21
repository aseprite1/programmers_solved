def solution(absolutes, signs):
    n= 0
    for i,j in zip(absolutes, signs):
        if j==1:
            n += i
        else:
            n += i*(-1)
    return n