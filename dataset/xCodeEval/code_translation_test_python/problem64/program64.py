def program64():
    import sys
    
    n,a,b,c = map(int,sys.stdin.readline().split())
    n=n%4
    mn=100000000000000
    for i in range(64):
        l=n
        sm=0
        aa=i%4
        sm+=a*aa
        l+=aa
        aa=i/4
        bb=aa%4
        l+=2*bb
        sm+=b*bb
        cc=aa/4
        l+=3*cc
        sm+=cc*c
        if l%4==0:
          if sm<mn:
            mn=sm
    
    print(mn)