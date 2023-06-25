def program238():
    from bisect import bisect_right
     
    n=int(input())
     
    l=[4,7]
    j=0
    for i in range(2000):
        l.append(l[j]*10+4)
        l.append(l[j]*10+7)
        j+=1
     
    l=[i for i in l if str(i).count('7')==str(i).count('4')]
     
    ind=bisect_right(l,n)
    if n in l:
        print(l[ind-1])
    else:
        print(l[ind])