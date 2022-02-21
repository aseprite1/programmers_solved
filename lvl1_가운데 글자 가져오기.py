def solution(s):
    if len(s)%2==0:
        j = int((len(s))/2)
        k = s[j-1:j+1]
    else:
        j = int((len(s)-1)/2)
        k = s[j:j+1]
    return k