def solution(left, right):
    p=0
    answer=0
    for i in range(left,right+1):
        for k in range(1,i+1):
            if i%k==0:
                p+=1
        if p%2==0:
            answer+=i
        else:
            answer-=i
        p=0
    return answer
