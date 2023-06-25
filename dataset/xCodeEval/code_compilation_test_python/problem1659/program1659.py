def program1659():
    n=int(input())
    x=0
    year=n+1
    if (n%4==0 and n%100!=0) or n%400==0:
        vis=True
    else:
        vis=False
    while x%7!=0 or x==0:
        
        if (year%4==0 and year%100!=0) or year%400==0:
            x+=2
            year+=1
            if not vis and x%7==0:
                x=0
        
        if vis:
            year+=1
            continue
        else:
            year+=1
            x+=1
            
    if vis:
        print(year-2)
    else:
        print(year-1)