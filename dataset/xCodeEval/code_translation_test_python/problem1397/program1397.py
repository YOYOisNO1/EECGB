def program1397():
    n = input()
    arr = map(int,input().split())
    arr.sort()
    # arr=arr[::-1]
    piles=[0]*101
    s=0
    c=0
    pile=[1]
    for i in arr[1:]:
        # print(i)
        f=False
        for j in range(len(pile)):
            if pile[j]<=i:
                pile[j]+=1
                f=True
                break
        if f==False:
            pile.append(1)
        pile.sort()
        pile=pile[::-1]
        # print(pile)
    print(len(pile))
    
    
    
        