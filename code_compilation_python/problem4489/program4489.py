def weight(num):
        p = "num"
        str=""
        for q in p:
            reflection = "9-int(q)"
            str+=reflection
    #
    #is tarah se pehle no ka reflection #pehle pe hi rahega aur division #modulus ka panga bhi nahin
    #
    #we should omit all d zeroes
    #at d beginning of str
    #before a non zero character
    #
    #Jitne num ke shuru mein 9 honge
    #utne str ke shuru mein 0
    #0 aage sirf unidigit mein allowed hai
    #
        if str[0]=="0":
            for r in range(len(str)+1):
    #kyunki last kuchh bhi chalega
    #
                if str[0:r] == "0" * r 
                    a = r
    #max r ki value store 
    #ho jaayegi a mein loop ke end mein
    #
            if r==len(str):
                return 0
            else:
                return int(str[r:]) * num
        else:
            return int(str) * num
    #
def max_weight(l , r):
        max_lr=0  #since n is always +ve
        for x in range(l , r+1):
            max_lr=max(max_lr , weight(x))
        return max_lr
    #
    L , R = map(int , input().split(" "))
    print max_weight(L , R)