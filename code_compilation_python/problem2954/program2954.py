    n=int(input())
def verif (a):
        if a%2==0:
            return (False)
        if a%3==0:
            return (False)
        if a%5==0:
            return (False)
        if a%7==0:
            return (False)
        return (True)
    s=0
    for i in range (1,n+1):
        if verif(i):
            s+=1
    print(s)
            