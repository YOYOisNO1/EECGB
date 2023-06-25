def AddBits(b1,b2):
        result=int(b1)+int(b2)
        if result==2:
            return (0,1)
        elif result==1:
            return (1,0)
        else:
            return (0,0)
    
    n=int(input())
    bit_num=input()
    
    bit_num_rev=''
    
    for i in range(n-1,-1,-1):
        bit_num_rev+=bit_num[i]
    
    revbits=0
    for i in range(len(bit_num_rev)-1,-1,-1):
        if i==len(bit_num_rev)-1:
            s,carry=AddBits(bit_num_rev[i],1)
        else:
            s,carry=AddBits(bit_num_rev[i],carry)
        #print(s,carry,bit_num_rev[i])
        if s!=int(bit_num_rev[i]):
            revbits+=1
        #print(revbits)
    
    print(revbits)
    