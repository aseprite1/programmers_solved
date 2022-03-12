def solution(s):
    k=[]
    for i in s:
        if len(k)==0:
            k.append(i)
        elif k[-1]==i:
            k.pop()
        else:
            k.append(i)
    if len(k)==0:
        return 1
    else:
        return 0