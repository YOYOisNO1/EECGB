def program6811():
    
    k = int(input())
    
    s = input()
    
    n = len(s)
    
    c = -1
    mp = {}
    arr = list(s)
    for i in range(1+n//2):
        if arr[i]==arr[n-i-1]:
            pass
    
                
        else:
            if arr[i]=='?':
                arr[i] = arr[n-i-1]
            else:
                if arr[n-i-1]=='?':
                    arr[n-i-1]=arr[i]
        if arr[i] in mp or arr[i]=='?':
            pass
        else:
            mp[arr[i]]=1
            c+=1;
    c = 0
    
    for x in range(k):
        if chr(ord('a')+x) in mp:
            pass
        else:
            mp[chr(ord('a')+x)]=0
            
        
    #print(mp)
    for i in range(n//2,-1,-1):
        if arr[i]==arr[n-i-1]:
            if arr[i]=='?':
                fl = 0
                for j in range(k-1,-1,-1):
                    if mp[chr(ord('a')+j)]==0:
                        arr[i],arr[n-i-1] = chr(ord('a')+j),chr(ord('a')+j)
                        mp[chr(ord('a')+j)]=1
                        fl = 1
                        break
                if fl==0:
                    arr[i],arr[n-i-1] = chr(ord('a')),chr(ord('a'))
                        
                        
    
    fl = 0
    mp = {}
    d = 0
    for i in range(1+n//2):
        if arr[i]!=arr[n-i-1]:
            fl = 1
        else:
            if arr[i] not in mp:
                d+=1;
                mp[arr[i]]=1
            
    #print(arr)
    if fl==1 or d!=k:
        print("IMPOSSIBLE")
    else:
        ar = sorted(mp.keys())
        c = 0
        fll = 0
        #print(ar)
        for x in ar:
            if ord(x)==ord('a')+c:
                pass
            else:
                fll = 1
            c+=1
        if fll == 1:
            print("IMPOSSIBLE")
        else:
            for x in arr:
                print(x,end="")