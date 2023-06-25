def program7560():
    n,m,k=map(int,input().split())
    if n%2==0:
        print("Marsel")
    else:
        for z in range(2,int(m**0.5)+2):
            if m%z==0 and m//z>=k:
                print("Timur")
                break
        else:
            if k==1 and m>1:
                print("Timur")
            else:
                print("Marsel")
            