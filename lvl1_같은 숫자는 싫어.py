def solution(arr):
    k = []
    for i in range(0,len(arr)-1):
        if arr[i] != arr[i+1]:
            k.append(arr[i])
    k.append(arr[-1])
    return k