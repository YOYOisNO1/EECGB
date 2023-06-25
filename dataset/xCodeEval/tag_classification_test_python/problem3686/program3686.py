def program3686():
    a,b,c=map(int,input().split())
    
    print(['First','Second'][min(a,b)<2*c])