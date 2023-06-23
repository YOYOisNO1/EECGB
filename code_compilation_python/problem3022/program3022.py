def program3022():
    import numpy as np
    
    n=int(input())
    #n=606725
    if int(np.sqrt(n))==np.sqrt(n):
        print(0)
    
    else:
        st=str(n)
        L=len(st)
    
        subs = []
        for i in range(len(st)):
            for j in range(i, len(st)):
                if st[i:j + 1][0] !=0:
                    subs.append(st[i:j + 1])
    
        results=[]
        for x in subs:
            n=int(x)
            if int(np.sqrt(n)) == np.sqrt(n):
                results.append(L-len(x))
    
        if len(results) ==0:
            print(-1)
        else:
            print(min(results))