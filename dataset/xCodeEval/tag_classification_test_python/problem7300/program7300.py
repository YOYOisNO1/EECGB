def program7300():
    m,b=map(int,input().split())
    a = 0
    for i in range(b):
        a=max(a,(m*(b-i)*(m*(b-i)+1)//2)*(i+1)+i*(i+1)//2*(m*(b-i)+1))
    print(a)