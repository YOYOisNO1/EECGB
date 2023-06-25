    Reflection Codeforces..More efficient program...
...........................................def weight(num):
        p = str(num)
        st = ""
        count=0
        for character in p:
            reflection = str(9-int(character))
            st += reflection
        if st[0]=="0":
    #
    #we need to eliminate all d zeroesu #from d start till a non zejro is #encountered or d string lasts den #return 0 since unidigit 0 is allowedj
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
        m = len(str(l))
        n=len(str(r))  #since r > l so m>=n
        p=int((int("9" * n)) / 2)
        q=p+1
        ml=weight(l)
        mr=weight(r)
        mp=weight(p)
    #
        if m==n :
            if l==p or r==p or l==q or r==q:
                return mp
            elif r<p:
                return mr
            elif l>q:
                return ml
            else:
                return weight(min((p-l) , (r-q)))
        else:
            if r < p :
                return mr
            else:
                return mp
    #
    L , R = map(int , input().split(" "))
    print max_weight(L , R)