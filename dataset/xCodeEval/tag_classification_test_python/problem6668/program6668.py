    #Algorithm :
    #   1) Split into strings , remove zeros
    #   2) Start checking for every integer in a range of(2 to 61) 
    #   3) check the numbers and respetively add them !
        
    ################################    
        
    #Function to calculate the value 
    #This function is approximately called 60 times by 2 strings ! And it still works
def base(t,b):
        num = 0
        p = 1
        i = len(t) - 1
        v = 0
        while i >=0 :
            if(t[i].isdigit()):
                v = int(t[i])  
            else:
                #Important to convert alphabets to numbers 
                v = ord(t[i]) - 55
            #If a value in string is greater than the numeral , then there can't exist such a numeral system 
            if v >= b:
                return -1
            num = num + (v*p)
            p=p*b
            i=i-1
        return num
            
    ###################################
    
    #Function to remove leading zeros    
def remove_zeros(s):
        i=0
        res=""
        while i < len(s) and s[i] == "0":
            i=i+1
        while i < len(s):
            res = res + s[i]
            i=i+1
        if res == "":
            res = "0"
        return res
    
    #####################################
        
    s = input().split(":")
    num = []
    for i in range(2):
        s[i]=remove_zeros(s[i]) 
    
    #Important range used for checking 
    for i in range(2,61):
        a = base(s[0],i)
        b = base(s[1],i)
        
        if a >= 0 and a <= 23 and b >=0 and b <= 59:
            num.append(i)
        
    if len(num) == 0:
        print(0)
    elif 60 in num :
        # As 60 cannot come it is possible only when there are only numbers at the 0th place 
        print(-1)
    else:
        for x in num:
            print(x)