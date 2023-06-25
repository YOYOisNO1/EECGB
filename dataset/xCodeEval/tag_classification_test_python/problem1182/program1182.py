def program1182():
    L=input
    R=print(a=L()+L())
    a,b=(ord(a[i])-ord(a[i+2])for i in(0,1))
    R(max(a,-a,b,-b))
    while a!=0 or b!=0:
     r=''
     if a<0:r='R';a+=1
     if a>0:r='L';a-=1
     if b<0:r+='U';b+=1
     if b>0:r+='D';b-=1
     R(r)