def program822():
    a,b,c=map(int,input().split());print(sum(map(int,input().split()[:a-b]))+b*c)