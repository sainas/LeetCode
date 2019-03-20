def myfun(k):
    if k ==1:
        return ['0','1']
    if k ==2:
        return['01','10','00']
    return list(map(lambda x: '0'+x,myfun(k-1)))+list(map(lambda x: '10'+x,myfun(k-2)))

print(myfun(3))