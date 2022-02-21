def solution(a, b):
    n = 0 
    for i,j in zip(a,b):
        n += i*j
    return n