def program610():
    n,p,k=map(int,input().split())
    if(p<1 or p>n):
        print(None)
    else:
        if(p-k>1 and p+k<n):
            print("<<"," ".join("(%d)"%(i) if i==int(((p-k)+(p+k))/2) else str(i) for i in range(p-k,p+k+1)),">>")
        elif(p-k<=1 and p+k>=n):
            print(" ".join("(%d)"%(i) if i==int(((p-k)+(p+k))/2) else str(i) for i in range(1,n+1)))
        elif(p-k>1):
            print("<<"," ".join("(%d)"%(i) if i==int(((p-k)+(p+k))/2) else str(i) for i in range(p-k,n+1)))
        elif(p+k<n):
            print(" ".join("(%d)"%(i) if i==int(((p-k)+(p+k))/2) else str(i) for i in range(1,p+k+1)),">>")