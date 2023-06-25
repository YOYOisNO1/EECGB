def checkDOB(a,b,c,d,e,f):
    # 1 incremented to use < instead of <= below(codegolfing)
     days=[32,29,32,31,32,31,32,32,31,32,31,32,32,30,32,31,32,31,32,32,31,32,31,32]
    # if(f-c>18 || (f-c==18 && (e-b>0 || (e-b==0&&d>=a) ) ) ):return true
     if( b<13 and e<13 and a<days[12*(c%4==0)+b-1] and d<days[12*(f%4==0)+e-1]):
      if(c-f>18 or (c-f==18 and ( b-e>0 or (b-e==0 and (  a>=d )  )  ) ) ):
     #  print(a,b,c,d,e,f)
       return True
     return False
    
    import sys
    #fi=open("G:\DUMP\input.in","r")
    #sys.stdin = fi
    i=0
    d=[]
    #for line in sys.stdin:
    for i in range(0,2):
     d+= input().replace('\n','').split(".")
    #print(d)
    for i in range(len(d)):
     d[i]=int(d[i])
    #print(d)
    b=False
    for i in range(3,6):
     for j in range(3,6):
      for k in range(3,6):
       if(i!=j and j!=k and k!=i):
        b|=checkDOB(d[0],d[1],d[2],d[i],d[j],d[k])
    print(["NO","YES"][b])
    #for x in 0,1:print"YNEOS"[x::2]