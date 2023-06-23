def program63():
    import numpy
    n=int(input())
    nu=[1]*10
    p=1
    while(p<n):
        for j in range(0,10):
            if(numpy.prod(nu)<n):
                nu[j]+=1
                p=numpy.prod(nu)
            else:
                break
    print('c'*nu[0]+'o'*nu[1]+'d'*nu[2]+'e'*nu[3]+'f'*nu[4]+'o'*nu[5]+'r'*nu[6]+'c'*nu[7]+'e'*nu[8]+'s'*nu[9])
    
    