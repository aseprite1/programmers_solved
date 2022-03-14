def solution(n):
    k,j,p=1,1,0
    for i in range(2,n):
        p=k
        k+=j
        j=p
    return k%1234567