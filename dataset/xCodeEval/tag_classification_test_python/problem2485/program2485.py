def program2485():
    n,k=map(int,input().split())
    j=n
    odd=3
    even=6
    if j%2==0:
        n1=1
        n2=1
    
    elif j%2!=0:
        n1=1
        n2=2
    
    preodd=1
    preeven=2
    if k==n:
        print(1)
    elif k==1:
        print(j)
    elif k==2:
        if j%2==0:
            print(j-2)
        else:
            print(j-1)
    else:
        pre=n
        j=n//2
        while (j >= 1):
            if j % 2 == 0:
                if pre % 2 == 0:
                    if (n1 + preodd+1) >= k:
                        ans = j
                        break
                    elif odd >= k:
                        ans = j - 1
                        break
                    elif even >= k and j > 4:
                        ans = j - 2
                        break
                    else:
                        n1 = (n1 + preodd + 1)
                        n2 = odd
    
    
                else:
                    if (n2 + preodd+1) >= k:
                        ans = j
                        break
                    elif odd >= k:
                        ans = j - 1
                        break
                    elif even >= k and j > 4:
                        ans = j - 2
                        break
                    else:
                        n1 = (n2 + preodd + 1)
                        n2 = odd
    
    
            else:
                if pre % 2 != 0:
                    if (n2 + 1) >= k:
                        ans = j
                        break
                    elif (preeven+n2+2) >= k:
                        ans = j - 1
                        break
                    elif odd >= k and j > 4:
                        ans = j - 2
                        break
                    elif even>=k and j>5:
                        ans=j-3
                        break
                    else:
                        n1 = (n2 + 1)
                        n2 = preeven+n2+2
    
                else:
                    if (n1 + 1) >= k:
                        ans = j
                        break
                    elif (n1+preeven+2) >= k:
                        ans = j - 1
                        break
                    elif odd >= k and j > 5:
                        ans = j - 2
                        break
                    elif even>=k and j>4:
                        ans=j-3
                        break
                    else:
                        n1 = (n1 + 1)
                        n2 = n1+preeven+2
            preodd = odd
            preeven = even
            odd = even + 1
            even = even + odd + 1
            pre = j
            j=j//2
    
    
    
    
    
        print(ans)
    
    
    
    