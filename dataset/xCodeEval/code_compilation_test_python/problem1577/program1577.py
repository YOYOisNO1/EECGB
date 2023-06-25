def program1577():
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    inf ="Finite"
    sum = 0
    for i in range(1,n):
        d = arr[i-1]+arr[i]
        if d==5 arr[i-1]==arr[i]:
            inf = "Infinite"
            break
        else:
            sum+=d
    
    print(inf)
    if(inf=="Finite"):
        print(sum)