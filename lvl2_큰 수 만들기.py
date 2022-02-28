def solution(number, k):
    answer_list = []
    ja = len(number) - k
    while k > 0:
        n = len(number)
        if (n-k-1) == 0:
            list_ = list(map(int, number))
        else:
            list_ = list(map(int, number[:-(n-k-1)]))
        if n == k:
            number = []
            break            
        a = max(list_)
        answer_list.append(a)
        b = number.index(str(a))
        number = number[b+1:]
        if n - len(number)-1 < 0:
            break
        k -= (n - len(number)-1)
    return ''.join(str(_) for _ in answer_list) + ''.join(str(_) for _ in number)

    # 8,10 런타임 에러

    def solution(number, k):
    digit=len(number)-k
    j = list(map(int, number))
    answer_list = []
    while digit>0:
        if '9' in j[:len(j)-digit+1]:
            num==9
        else:
            num=max(j[:len(j)-digit+1])
        j=j[j.index(num)+1:]
        answer_list.append(num)
        digit-=1
    return ''.join(map(str,answer_list))

    # 9,10 런타임 에러 