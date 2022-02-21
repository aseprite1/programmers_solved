def solution(array, commands):
    B = []
    for i in commands:
        K = array[ i[0]-1 : i[1]]
        A = K.copy()
        A.sort()
        B.append(A[i[2]-1])
    return B