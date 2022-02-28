def solution(x):
    k=[]
    s=0
    for i in str(x):
        k.append(i)
    for i in k:
        s+=int(i)
    if x%s==0:
        return True
    else:
        return False