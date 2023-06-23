def program2968():
    n=int(input())
    lst=[*set(map(int,input().split()))]
    lst.sort()
    for i,x in enumerate(lst[:-1]):
        item=int('1'*x,2)
        item=item*item
        if item.bit_length()>lst[i+1]:
            from sys import exit
            print('YES');exit()
    print('NO')