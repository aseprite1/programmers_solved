def solution(n):
    k=""
    while n!=0:
        if n%3==1:
            k+="1"
            n-=1
            if n==0:
                return (k[::-1])  
            else:
                n= n/3                       
        if n%3==2:
            k+="2"
            n-=2
            if n==0:
                return (k[::-1])  
            else:
                n= n/3
        if n%3==0:
            k+="4"
            n-=3
            if n==0:
                return (k[::-1])  
            else:
                n=n/3