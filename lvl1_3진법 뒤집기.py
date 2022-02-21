def solution(n):
    k = ''
    while n>0:
        n, mod = divmod(n,3)
        k+=str(mod)   
    return int(k,3)