    import sys
    sys.setrecursionlimit(1000000)
    
def proov(st):
        l=[i for i in st]
        g=l[:]
        g.sort()
        if g==l:
            return True
        else:
            return False
    
def rec(i,j):
        global l
        if l[i][j]=='':
            if s[i]==s[j]:
                d=s[i]
                d+=str(rec(i+1,j-1))
                d+=s[i]
           
                if proov(d):
                    l[i][j]=d
            else:
                t=rec(i+1,j)
                t2=rec(i,j-1)
                if proov(t)==False:
                    t=''
                if proov(t2)==False:
                    t2=''
                if len(t)>len(t2):
                    l[i][j]=t
                else:
                    l[i][j]=t2
        return l[i][j]
                
    
    s=input()
    n=len(s)
    l=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                l[i][j]=s[i]
            elif i<j:
                l[i][j]=''
            else:
                l[i][j]=0
    rec(0,n-1)
    
    print(l[0,n-1])