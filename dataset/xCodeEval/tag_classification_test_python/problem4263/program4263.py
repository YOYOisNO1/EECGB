def program4263():
    sticks=[int(i) for i in input().split()]
    flag=0
    for i in sticks:
        if(sticks.count(i)>=4):
            flag=1
            for j in range(1,5):
                sticks.remove(i)
    if(flag==0):
        print("Alien")
    else:
        if(sticks[0]==sticks[1]):
            print("Elephant")
        else:
            print("Bear")
        
            