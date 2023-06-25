def func (l,r):
        for i in range(l,r+1):
            s=str(i)
            if len(s)==len(set(s)):
                return i
        
        return -1
     
    if __name__=="__main__":
        l,r=map(int,input().split(" "))
        if l==r:
            if(len(str(l))==len(set(l)):
                print(l)
            else:
                
            print(-1)
        elif l>r:
            print(-1)
        else:
            x=func(l,r)
            print(x)