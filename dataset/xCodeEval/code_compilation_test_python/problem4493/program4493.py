def weight(num):
        p = str(num)
        st = ""
        count=0
        for character in p:
            reflection = str(9-int(character))
            st += reflection
        if st[0]=="0":
    #
    #we need to eliminate all d zeroes #from d start till a non zero is #encountered or d string lasts den #return 0 since unidigit 0 is allowed
    #
            for r in range(1 , len(st)+1):
                if st[0:r] == ("0") * r:
                    count+=1
                else:
                    break  
    #jaisa hi pehla non zero mila break d 
    #loop
    #max r ki value store 
    #ho jaayegi a mein loop ke end mein
    #
            if count == len(st):
                return 0
            else:
                return ((int(st[count:])) * num)
        else:
            return ((int(st)) * num)
    #
def max_weight(l , r):
        max_lr=0  #since n is always +ve
        for x in range(l , r+1):
            max_lr=max(max_lr , weight(x))
        return max_lr
    #
    L , R = map(int , input().split(" "))
    print max_weight(L , R)