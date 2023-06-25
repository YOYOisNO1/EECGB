def program2159():
    n=int(input())
    s=str(n)
    count=len(s)
    for i in range(0,len(s)):
        if s[i]=="4" or s[i]=="7":
            count=count-1
    if count==0 or n%4==0 or n%7==0 or n%47==0 or n%74==0 or n%477==0 or n%447==0 or n%774==0 or n%747==0 or n%474==0:
        print("YES")
    else:
        print("NO")
    