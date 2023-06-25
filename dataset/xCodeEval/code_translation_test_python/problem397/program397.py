def program397():
    n=input()
    pre=0
    set=5
    len=5
    while n>set:
        pre=set
        len=len*2
        set=set+len
    if pre!=0:
        mod=(n-pre-1)/(len/5)
    else:
        mod=n-pre-1
    name=['Sheldon','Leonard','Penny','Rajesh','Howard']
    print(name[mod])