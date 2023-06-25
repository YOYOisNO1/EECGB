def program1188():
    a=int(input())
    b=list(map(int,input().split()))
    m=max(b)
    for i in range (1,a-1):
        if  m>b[i+1]-b[i-1]:
            m=b[i+1]-b[i-1]
    for i in range(1,a):
        if m<b[i]-b[i-1]:
            m=b[i]-b[i-1]
    print(m)