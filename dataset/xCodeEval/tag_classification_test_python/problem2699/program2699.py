def program2699():
    n,B = map(int,input().split())
    a = input()
    A = list(map(int,list(a.split())))
    i = 0
    e = 0
    o = 0
    c = 0
    ls = []
    while(i<n):
        if A[i]%2 == 0:
            e = e+1
        else:
            o = o+1
        if o == e:
            if i == n-1:
                break
            else:
                ls.append(abs(A[i]-A[i+1]))
                o = 0
                e = 0
        i = i+1
    if ls == []:
        print(0)
    else:
        ls.sort()
        for i in ls:
            if i<=B:
                c = c+1
                B = B-i
            else:
                break
        print(c)
                
                    
    
     
            
            
     
     
     
     