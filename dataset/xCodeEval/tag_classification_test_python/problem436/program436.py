def program436():
    #!/bin/python2
    
    from sys import stdin
    
    cup = map(int,stdin.readline().strip().split())
    mad = map(int,stdin.readline().strip().split())
    shelf = int(stdin.readline().strip())
    cups=sum(cup)
    mads=sum(mad)
    required = cups/5 + mads/10
    if cups%5:
        required+=1
    if mads%10:
        required+=1
    if(required<=shelf):
        print("YES")
    else:
        print("NO")