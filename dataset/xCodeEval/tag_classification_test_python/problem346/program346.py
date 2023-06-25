def program346():
    n=int(input())
    if n<4:print(2*n+1);quit()
    print(4*((n-1)//3+1)+[3,0,1][n%3])