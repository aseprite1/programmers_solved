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