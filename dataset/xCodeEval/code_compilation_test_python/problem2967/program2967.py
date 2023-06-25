def program2967():
    n=input()
    l=sorted(list(set(map(int,input().split()))))
    print ['NO','YES'][n<2 and l[0]!=1) or (n>1 and l[-2]*2>l[-1])]