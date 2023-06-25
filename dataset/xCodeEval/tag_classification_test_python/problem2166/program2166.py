def program2166():
    
    if __name__== "__main__":
        n=input()
        a=map(int,input().split())
        b=map(int,input().split())
        aa=[0]*7
        bb=[0]*7
        for i in range(n):
            aa[a[i]]+=1
            bb[b[i]]+=1
        s=f=0
        for i in range(1,6):
            if (aa[i]+bb[i])%2:
                f=1
                print("-1")
                break
            else:
                s+=((aa[i]+bb[i])/2-min(aa[i],bb[i]))
        if f==0:
            print(s/2)