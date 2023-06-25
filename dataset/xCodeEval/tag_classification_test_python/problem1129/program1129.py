def program1129():
    from sys import stdin
    
    n = int(stdin.readline())
    a = [int(i) for i in stdin.readline().split(" ")]
    b = []
    for i in a:
        b.append(1) if i>0 else b.append(0)
    
    s = sum(a)
    
    count = 0
    
    while n>0:
        if b[count]==1:
            n = n-a[count] 
        if n<=0:
            break
        count += 1
        count = count%7
    print(count+1)