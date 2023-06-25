    #!/usr/bin/python
    import math
    l=0
    lst=[]
    gcd = lambda a,b: gcd(b%a, a) if a else b
    lcm = lambda a,b: a*b/gcd(a,b)
def dfs(a,v,i):
        global l
        v[i]=1
        l+=1
        if v[a[i]]==-1:
            return (dfs(a,v,a[i]))
        else :
            return (a[i],l)
        
    
def main():
        global l
        n=int(input())
        a=map(int,input().split(' '))
        for i in range(0,n):
            a[i]-=1
        for i in range(0,n):
            v=[-1]*105
            l=0
            temp=dfs(a,v,i)
            if temp[0]!=i:
                print("-1")
                return
            if temp[1]%2 == 1:
                lst.append(temp[1])
            else :
                lst.append(temp[1]/2)
        ans=1
        for i in range(0,n):
            ans=lcm(ans,lst[i])
        print(ans)
    if __name__=='__main__':
        main()