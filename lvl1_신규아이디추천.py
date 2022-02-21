from string import ascii_lowercase
def solution(new_id):
    k = new_id.lower()
    o = k
    for i in o:
        if i not in list(ascii_lowercase) and i not in ['-','_','.','0','1','2','3','4','5','6','7','8',"9"]:
            k = k.replace(i,"")
# 2단계 끝
    while '..' in k:
        k = k.replace("..",".")

# 3단계 끝
    if k!='':
        if k[0]=='.':
            k = k[1:]
        if k!='':
            if k[-1]=='.':
                k = k[:-1]
# 4단계 끝
    if k=='':
        k = "a"
# 5단계 끝
    if len(k)>=16:
        k = k[:15]
        if k[-1]=='.':
            k = k[:-1]
# 6단계 끝
    if len(k)<=2:
        k = k + k[-1]*(3-len(k))
    return k