def program119():
    n=int(input())
    l=list(map(int,input().split()))
    if len(l)<=3:
        print(l[2]-l[0])
    else:
        A=[]
        B=[]
        for i in range(len(l)):
            if i!=len(l)-1 and i!=0:
                
              a=l.pop(i) 
              for j in range(len(l)):
                  if   j!=len(l)-1:
                   A.append(l[j+1]-l[j])
              B.append(max(A))
              A=[]
              l.append(a)
              l.sort()
    
    print(min(B))
            
            