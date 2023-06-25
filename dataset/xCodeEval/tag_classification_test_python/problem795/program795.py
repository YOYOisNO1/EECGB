    a,b = map(int,input().split())
    
def found_n(x,a):
        n = 0
        while(2**n-1  < x ):
            n+=1
    
        number = list(bin(2**n-1))
        conta = 0
        # print('n=',n)
        for i in range(2, 2+n):
            number_ = list(number)
            number_[i]='0'
            # print(number_)
            number_ = ''.join(number_)
            if (int(number_,2) != (2**(n-1)-1)):
                if (a):
                    if (int(number_,2) <= x):
                        # print('opa ',int(number_,2),bin(int(number_,2)),'i=',i)
                        conta+=1
                else:
                    if (int(number_,2) < x):
                        # print('opa ',int(number_,2),bin(int(number_,2)))
                        conta+=1
    
        # print('conta=',conta)
        soma = (n*(n-1))//2 - (n-1) + 1
        # print('soma=',soma)
        total = conta + soma
        return total
    
    b_ = found_n(b,True)
    a_ = found_n(a,False)
    
    print(b_-a_)