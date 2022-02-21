def solution(arr):
    k=min(arr)
    if len(arr)==1:
        return [-1]
    else:
        arr.remove(k)
        return arr