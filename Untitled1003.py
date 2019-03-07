def valid(S):
    if len(S)%3!=0:
        return False
    begin=beginf(S)
    if begin == len(S):
        return True
    if begin == 1:
        return False
    endw = endf(S)
    if endw == len(S):
        return False
    newstr=S[0:begin-1]+S[endw:]
    subs=S[begin-1:endw]
    if not valid(newstr):
        return False
    elif not valid(subs):
        return False
    return True
def beginf(S):
    v='abc'
    for i in range(len(S)):
        if S[i]!=v[i%3]:
            return i+1
    return len(S)
def endf(S):
    v='cba'
    for i in range(len(S)):
        if S[-i-1]!=v[i%3]:
            return len(S)-i

print(valid('abcaabcbc'))