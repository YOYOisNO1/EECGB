def program4338():
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    from collections import defaultdict
    al=defaultdict(int)
    import math
    if(b==d):
        print(b)
        exit()
    else:
        if(b>d):
            rem=[]
            b=b-d
            while(1):
                if(b%c==0):
                    print(b+d)
                    exit()
                else:
                    al[b%c]+=1
                    if(al[b%c]>1):
                        print(-1)
                        exit()
                    else:
                        b+=a
        else:
            rem=[]
            d=d-b
            while(1):
                if(d%a==0):
                    print(b+d)
                    exit()
                else:
                    al[d%a]+=1
                    if(al[d%a]>1):
                        print(-1)
                        exit()
                    else:
                        d+=c
            
                    
                
                
           