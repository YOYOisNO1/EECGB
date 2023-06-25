def program444():
    # import sys
    # sys.stdin = open('test.txt','r')
    
    n,c = map(int,input().split())
    x = map(int,input().split())
    print(max(max([x[i]-x[i+1]-c) for i in range(len(x)-1)]),0)