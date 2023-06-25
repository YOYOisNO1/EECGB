def program2986():
    import math
    i1=int(input())
    a=1
    b=i1
    for i in range(2,int(i1**(1/2))+1):
        if(i1%i==0 and math.gcd(i,i1//i)==1):
            a=i
            b=i1//i
    print(a,b)