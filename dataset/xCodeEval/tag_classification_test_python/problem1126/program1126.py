def program1126():
    n=input()
    a,b,c=map(int,input().split())
    d,e,f=map(int,input().split()) 
    k=max(0,a-d-f)+max(0,b-e-d)+max(0,c-f-e)
    j=min(a,e)+min(b,f)+min(c,d)
    print(k,j)