def solution(arr):
    k=0
    for i in arr:
        k+=i
    s=k/len(arr)
    return s