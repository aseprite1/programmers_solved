def solution(n):
    k="" 
    if n%2==0:
        k=k+"수박"*(n//2)
    else:
        k=k+"수박"*((n-1)//2)+"수"
    return k