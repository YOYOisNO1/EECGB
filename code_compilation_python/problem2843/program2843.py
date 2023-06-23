def program2843():
    import sys
    
    n=int(input())
    s=input()
    Count=1
    i=0
    while(i<n):
        sys.stdout.write(s[i])
        i+=Count
        Count+=1
    print ''