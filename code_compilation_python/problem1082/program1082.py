def program1082():
    from functools import reduce
    n=int(input())
    l=list(map(int,input()))
    print(reduce(lambda x,y:abs(x)+abs(y) , l)