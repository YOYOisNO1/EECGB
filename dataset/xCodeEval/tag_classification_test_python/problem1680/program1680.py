def program1680():
    from bisect import*;input();l,a=[],''
    for c in[-ord(i)for i in input()]:
     i=bisect_left(l,c);a+=str(i)
     if i<len(l):l[i]=c
     else:l+=c,
    if len(l)<3:print('Yes');print(a)
    else:print('No')