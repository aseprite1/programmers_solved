def solution(numbers):
    k=0
    for i in range (1,10):
        if i in numbers:
            k+=i
    return 45-k