from itertools import combinations 
def solution(nums):
    e=0
    for i in list(combinations(nums, 3)):
        k=0
        n=sum(i)        
        for j in range(2,n):
            if (n%j)==0:
                k+=1
        if k==0:
            e+=1
    return e